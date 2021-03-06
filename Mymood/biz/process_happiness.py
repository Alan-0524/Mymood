from models_app.models import *
import uuid
import time
import datetime
from django.db.models import Max, Avg, F, Q
from django.utils.timezone import now, timedelta
from django.http import HttpResponse
import csv


def query_all_happiness(request, for_who):  # 动态查询所有心情数据
    startDate = request.POST.get("startDate")
    endDate = request.POST.get("endDate")
    query_type = request.POST.get("query_type")
    team_id = request.POST.get("team_id")
    date_type = "day"
    start_date = now().date() + timedelta(days=-30)  # before 30 days
    end_date = now().date()
    date_range = (start_date, end_date)

    if startDate is not None and endDate is not None:
        date_range = (startDate, endDate)
        start_sec = time.mktime(time.strptime(startDate, '%Y-%m-%d'))  # Conversion date format
        end_sec = time.mktime(time.strptime(endDate, '%Y-%m-%d'))  # Conversion date format
        work_days = int((end_sec - start_sec) / (24 * 60 * 60))  # Calculating the difference
        if work_days >= 30:
            date_type = "month"

    if query_type == "query_teams":
        list_target = TblTeam.objects.all()
    if query_type == "query_individuals":
        list_target = TblUser.objects.filter(team_id=team_id)
    if query_type is None or query_type == "":
        list_target = [0]
    list_happiness = organize_happiness_data(query_type, date_type, date_range, list_target, for_who)
    # js_data = json.dumps(list_happiness)
    return list_happiness


def organize_happiness_data(query_type, date_type, date_range, list_target, for_who):  # 组织所要展现的数据
    conter_max = [0, 0]
    list_tep = []
    list_queryset = []
    list_happiness = []
    x = ['x']
    select = {date_type: 'extract( ' + date_type + ' from date )'}
    for i in range(0, len(list_target)):  # 组织团队数据
        if query_type == "query_teams":
            team = list_target.__getitem__(i)
            team_id = team.team_id
            team_name = team.name
            list_data = [team_name]
            list_queryset = TblHappiness.objects.filter(date__range=date_range,
                                                        team_id=team_id).extra(
                select=select).values(date_type).annotate(avg=Avg(for_who))

        if query_type == "query_individuals":  # 组织个人数据
            user = list_target.__getitem__(i)
            user_id = user.user_id
            list_data = ["member_" + str(i) + ""]
            list_queryset = TblHappiness.objects.filter(date__range=date_range,
                                                        user_id=user_id).extra(
                select=select).values(date_type).annotate(avg=Avg(for_who))

        if query_type is None or query_type == "":  # 按类型查询
            list_data = ["whole"]
            list_queryset = TblHappiness.objects.filter(date__range=date_range).extra(
                select=select).values(date_type).annotate(avg=Avg(for_who))

        if len(list_queryset) > conter_max[1]:
            conter_max[0] = i
            conter_max[1] = len(list_queryset)
        list_tep.append(list_queryset)

        if len(list_queryset) is not 0:
            for k in range(0, len(list_queryset)):
                avg = list_queryset.__getitem__(k).get('avg')
                list_data.append(avg)
        else:
            list_data.append(0)
        list_happiness.append(list_data)

    if len(list_tep) is not 0:
        max_number_items = list_tep.__getitem__(conter_max[0])
        if len(max_number_items) is not 0:
            for j in range(0, len(max_number_items)):
                date = max_number_items.__getitem__(j).get(date_type)
                x.append(date)
        else:
            x.append(0)
    else:
        x.append(0)
    list_happiness.insert(0, x)

    return list_happiness


def save_happiness(own, team, user_id):  # 保存心情数据
    user = TblUser.objects.get(user_id=user_id)
    team_id = user.team_id
    happiness = TblHappiness()
    happiness.id = str(uuid.uuid1()).replace("-", "")
    happiness.user_id = user_id
    happiness.team_id = team_id
    happiness.idvl_hpns = own
    happiness.team_hpns = team
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  # 格式化时间
    happiness.date = time_now
    happiness.save()
    if user.first_time_status == 0 and user.second_time_status == 0:
        user.first_time_status = 1
    elif user.first_time_status == 1 and user.second_time_status == 0:
        user.second_time_status = 1
    user.save()


def save_happiness_level(happiness_level):  # 保存心情数据
    happiness = happiness_level.split("&")  # 分割数据
    user_id = happiness[0]
    idvl = happiness[1]
    team = happiness[2]
    save_happiness(idvl, team, user_id)


def query_team_happiness(request):  # 查询心情数据
    try:
        user_id = request.GET.get("user_id")
        date_range = date_filter(request)
        list_user = TblHappiness.objects.filter(date=date_range, user_id=user_id)
    except Exception as e:
        print("Error info:----------------", e)


def date_filter(request):  # 过滤查询
    if 'year_from' and 'month_from' and 'day_from' and \
            'year_to' and 'month_to' and 'day_to' in request.GET:
        y = request.GET['year_from']
        m = request.GET['month_from']
        d = request.GET['day_from']
        date_from = datetime.datetime(int(y), int(m), int(d), 0, 0)
        y = request.GET['year_to']
        m = request.GET['month_to']
        d = request.GET['day_to']
        date_to = datetime.datetime(int(y), int(m), int(d), 0, 0)
        date_range = (date_from, date_to)
        print(date_range)
        return date_range
    else:
        print("error time range!")


def export_csv():  # 导出数据
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="happiness.csv"'
    writer = csv.writer(response)
    happness_list = TblHappiness.objects.all()

    for i in range(0, len(happness_list)):  # 写入每行数据
        happiness = happness_list.__getitem__(i)
        writer.writerow(['member;'])
        writer.writerow(['team_id:'])
        writer.writerow([happiness.team_id])
        writer.writerow(['date'])
        writer.writerow([str(happiness.date)[:10]])
        writer.writerow(['for work'])
        writer.writerow([str(happiness.idvl_hpns)])
        writer.writerow(['for teams'])
        writer.writerow([str(happiness.team_hpns)])
    return response
