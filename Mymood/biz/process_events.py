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
        text = text + "<tr><td>" + event.event_title + "</td><td>" + str(event.event_date)[

                                                                     :10] + "</td><td>" + event.event_content + "</td></tr>"
    # Translation string to html
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
