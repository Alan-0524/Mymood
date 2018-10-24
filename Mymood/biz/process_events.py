from models_app.models import *
import uuid
import html


def query_events():
    # Get all objects
    event_list = TblEvent.objects.all()
    text = str("")
    # Loop list
    for i in range(0, len(event_list)):
        # put objects in string of Html
        event = event_list.__getitem__(i)
        text = text + "<tr><td><a href='javascript:void(0)'><i class='fa fa-edit' onclick=""edit_event('" + event.id + "')""></i></a></td><td><a href='javascript:void(0)'><i class='fa fa-minus-square-o' onclick=""delete_event('" + event.id + "')""></i></a></td><td><a href='javascript:void(0)' onclick=""event_detail('" + event.id + "')"">" + str(
            event.event_title)[:40] + "</a></td><td>" + str(
            event.event_date)[:10] + "</td><td>" + str(event.event_content)[:40] + "...</td></tr>"
    # Translation string to html
    html_text = html.unescape(text)
    return html_text


def event_detail(request):  # 查询书细节
    id = request.POST.get("id")
    event = TblEvent.objects.get(id=id)
    text = "<p>Event title:" + event.event_title + "</p><p>Event date:" + str(event.event_date)[
                                                                          :10] + "</p><p>Event content:" + event.event_content + "</p>"
    html_text = html.unescape(text)
    return html_text


def save_event(request):  # 保存数据
    try:
        id = request.POST.get("id")
        if id != "" and id is not None:
            event = TblEvent.objects.get(id=id)
        else:
            event = TblEvent()
            event.id = str(uuid.uuid1()).replace("-", "")
        event.event_title = request.POST.get('event_title')
        event.event_date = request.POST.get('event_time')
        event.event_content = request.POST.get('event_content')
        event.save()
    except Exception as e:
        print("Error info:----------------", e)
        return "error"
    return "success"


def get_event(request):  # 获取事件
    try:
        id = request.POST.get("id")
        event = TblEvent.objects.get(id=id)
        data = {"id": event.id, "title": event.event_title, "date": event.event_date, "content": event.event_content}
        return data
    except Exception as e:
        return "error"


def delete_event(request):  # 删除事件
    try:
        id = request.POST.get("id")
        event = TblEvent.objects.get(id=id)
        event.delete()
        return "success"
    except Exception as e:
        return "error"
