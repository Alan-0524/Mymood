from models_app.models import *



def save_event(request):
    try:
        event = TblEvent()
        event.id = str(uuid.uuid1()).replace("-", "")
        event.event_title = request.POST.get('event_title')
        event.event_date = request.POST.get('event_time')
        event.evenequest.POST.get('event_content')
        event.save()
    except Exception as e:
        print("Error info:----------------", e)
        return "error"
    return "success"
