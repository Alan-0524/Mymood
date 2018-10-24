from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Mymood.biz import process_happiness, process_teams, process_members, process_events
from django.utils.timezone import now, timedelta
from models_app.models import TblUser
from django.views.decorators.http import require_http_methods


# 跳转主页
def mood(request):
    base_url = request.get_raw_uri()
    request.session['base_url'] = base_url
    return render(request, 'response/pages-sign-in.html')


# 登录
def sign_in(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")
        try:
            user = TblUser.objects.get(user_name=user_name)  # 查询用户
            if check_password(password, user.password) is True:  # 登录验证密码
                request.session['is_login'] = True
                request.session['user_id'] = user.user_id
                request.session['user_name'] = user.user_name
                # request.session.get('is_login', None)
                role = ""
                if user.role == 0:  # 判断角色
                    role = "Administrator"
                if user.role == 1:
                    role = "Researcher"
                data = {
                    'user_name': user.user_name,
                    'user_role': role
                }
                return render(request, 'response/index.html', data)
            else:
                message = "Wrong user name or password!"
        except Exception as e:
            print(e)
            message = "User does not exist!"
    else:
        return render(request, 'response/pages-sign-in.html')
    return render(request, 'response/pages-sign-in.html', {'status': message})


def redirect_sign_up(request):
    return render(request, 'response/pages-sign-up.html')


# 注册
def sign_up(request):
    try:
        result = process_members.create_researcher(request)  # 执行注册方法

        if result == "success":
            return render(request, 'response/pages-sign-in.html')
        else:
            return render(request, 'response/pages-sign-up.html', {'status': 'User already exists!'})
    except Exception as e:
        print("Error info:----------------", e)
        return render(request, 'response/pages-sign-up.html', "System exception!")


@require_http_methods(["GET"])
def get_webhook(request, psid):
    result = process_members.query_member(psid)  # 查询用户是否已存在
    if result is True:
        data = {
            'status': '1',  # 存在
        }
    elif result is False:
        data = {
            'status': '0',  # 不存在
        }
    else:
        data = {
            'status': '9',  # 错误
        }
    return JsonResponse(data, safe=False)


@require_http_methods(["GET"])
def save_happiness_level(request, happiness_level):  # 保存心情数据
    try:
        process_happiness.save_happiness_level(happiness_level)  # 处理保存
        data = {
            'status': '0',  # 成功
        }
    except Exception as e:
        data = {
            'status': '1',  # 失败
        }
    return JsonResponse(data, safe=False)


def select_emoji(request, user_id):  # 选择心情
    base_url = request.get_host()
    request.session['base_url'] = base_url
    context = {
        'user_id': user_id,
    }
    return render(request, 'response/select-emoji.html', context)


def submit_emoji(request):  # 保存心情数据
    data = request.POST
    own = data.get('own')
    team = data.get('team')
    user_id = data.get('user_id')
    process_happiness.save_happiness(own, team, user_id)  # 处理保存
    ret = {"status": 0, 'url': ''}
    return JsonResponse(ret)


def register_messenger(request, user_id):  # 注册成员
    base_url = request.get_host()
    request.session['base_url'] = base_url
    context = {
        'user_id': user_id,
    }
    return render(request, 'response/register_messenger_independent.html', context)


def submit_register(request):  # 保存成员数据
    data = request.POST
    user_name = data.get('user_name')
    user_id = data.get('user_id')
    result = process_members.create_members(user_id, user_name, "")  # 处理数据
    ret = {"status": result}
    return JsonResponse(ret)


def query_happiness(request):
    happiness_list_teams = process_happiness.query_all_happiness(request, 'team_hpns')  # 查询team的心情数据
    happiness_list_individuals = process_happiness.query_all_happiness(request, 'idvl_hpns')  # 查询个人心情数据
    team_list = process_teams.query_all_teams(request)  # 查询所有
    start_date = now().date() + timedelta(days=-30)  # before 30 days
    end_date = now().date()
    context = {'happiness_list_teams': happiness_list_teams, 'happiness_list_individuals': happiness_list_individuals,
               'team_list': team_list, 'start_date': start_date, 'end_date': end_date}
    return render(request, 'response/charts-c3.html', context)


def refresh_happiness(request):  # 刷新心情数据
    happiness_list_teams = process_happiness.query_all_happiness(request, 'team_hpns')
    happiness_list_individuals = process_happiness.query_all_happiness(request, 'idvl_hpns')
    context = {'happiness_list_teams': happiness_list_teams, 'happiness_list_individuals': happiness_list_individuals}
    return JsonResponse(context)


def export_csv(request):  # 登录导出数据源
    # response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="happiness.csv"'
    # writer = csv.writer(response)
    #
    # happiness_list_teams = process_happiness.query_all_happiness(request, 'team_hpns')
    # happiness_list_individuals = process_happiness.query_all_happiness(request, 'idvl_hpns')
    #
    # writer.writerow(['For teams'])
    # for i in range(0, len(happiness_list_teams)):
    #     happiness_data_teams = happiness_list_teams[i]
    #     writer.writerow(happiness_data_teams)
    # writer.writerow([''])
    # writer.writerow([''])
    # writer.writerow(['For owns'])
    # for j in range(0, len(happiness_list_individuals)):
    #     happiness_data_teams = happiness_list_individuals[j]
    #     writer.writerow(happiness_data_teams)
    response = process_happiness.export_csv()
    return response


def switch_members(request):  # 分配用户至某个组
    result = process_members.switch_members(request)  # 处理分配
    if result == "success":
        ret = {"status": 0}
    else:
        ret = {"status": 1}
    return JsonResponse(ret)


def jump_members_in_teams(request):  # 页面跳转
    team_list = process_teams.query_all_teams(request)  # 查询tean list
    context = {'team_list': team_list}
    return render(request, 'response/members-table.html', context)


def query_members_in_teams(request):  # 查询tean list
    html_text = process_members.query_members_in_teams(request)
    context = {
        'html_text': html_text,
    }
    return JsonResponse(context)


def jump_teams(request):  # 跳转至team页面
    return render(request, 'response/teams-table.html')


def load_teams(request):
    html_text = process_teams.load_teams(request)  # 动态加载team
    context = {
        'html_text': html_text,
    }
    return JsonResponse(context)


def check_team_name(request):  # 检查team是否已存在
    result = process_teams.check_team_name(request)
    if result is True:
        ret = {"status": 1}
    if result is False:
        ret = {"status": 0}
    return JsonResponse(ret)


def create_teams(request):  # 创建 team
    result = process_teams.create_teams(request)
    ret = {"status": result}
    return JsonResponse(ret)


def get_team(request):  # 查询单个team
    data = process_teams.get_team(request)
    if data != "error":
        ret = {"data": data}
    else:
        ret = {"data": "error"}
    return JsonResponse(ret)


def delete_team(request):  # 删除team
    status = process_teams.delete_team(request)
    ret = {"status": status}
    return JsonResponse(ret)


def jump_events(request):  # 跳转至 event页面
    context = {'event_list': 'event_list'}
    return render(request, 'response/events-table.html', context)


def query_events(request):  # 查询event
    html_text = process_events.query_events()
    context = {
        'html_text': html_text,
    }
    return JsonResponse(context)


def save_event(request):  # 保存event
    result = process_events.save_event(request)
    if result == "success":
        ret = {"status": 0}
    else:
        ret = {"status": 1}
    return JsonResponse(ret)


def get_event(request):  # 获取单个event
    data = process_events.get_event(request)
    if data != "error":
        ret = {"data": data}
    else:
        ret = {"data": "error"}
    return JsonResponse(ret)


def delete_event(request):  # 删除event
    status = process_events.delete_event(request)
    ret = {"status": status}
    return JsonResponse(ret)


def event_detail(request):
    html_text = process_events.event_detail(request)
    context = {
        'html_text': html_text,
    }
    return JsonResponse(context)


def query_teams(request):
    html_text = process_teams.query_teams_html(request)
    context = {
        'html_text': html_text,
    }
    return JsonResponse(context)


def success(request):
    return render(request, 'response/success.html')
