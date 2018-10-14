from models_app.models import *
import uuid
import html


def query_events():
    event_list = TblEvent.objects.all()
    text = str("")
    for i in range(0, len(event_list)):
        event = event_list.__getitem__(i)
        text = text + "<tr><td>" + event.event_title + "</td><td>" + str(event.event_date)[:10] + "</td><td>" + event.event_content + "</td></tr>"
    html_text = html.unescape(text)
    return html_text


def save_event(request):
    try:
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
