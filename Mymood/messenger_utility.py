import requests
import urllib3
import json
import certifi


def push_notifications(id):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    apiUrl = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAE358wDWxQBANcfxlUa3tfs7DPhsrrtJN8Q8AWvE7tvq3RdErlFyfHDKY8SMZBHR4YTK8fJkxW054ZAKDDfgXVkXzb0VPvj9gg2ZBs7rBI8k6Yt263vaxGMlBmsxks5oWfkiT7w2Uh5LiCeAll3lYfvpT7oFedMTiHaQMp7l60yVjJvhZAc'
    recipient = {'id': id}
    # message = {
    #     'attachment': {'type': 'template',
    #                    'payload': {'template_type': 'button', 'text': 'Hello! It is time to enter your happiness.😁',
    #                                'buttons': [{
    #                                    "type": "web_url",
    #                                    "url": "https://mymood-service.herokuapp.com/select_emoji/"+id+"/",
    #                                    "title": "Tell me 👇",
    #                                    "webview_height_ratio": "full",
    #                                    "messenger_extensions": "true",
    #                                }]}}}
    message = {"text": "Hello! What is your current state of happiness about your work in this team?😁",
               "quick_replies": [
                   {"content_type": "text", "title": "😁", "payload": "5"},
                   {"content_type": "text", "title": "🙂", "payload": "4"},
                   {"content_type": "text", "title": "😐", "payload": "3"},
                   {"content_type": "text", "title": "😔", "payload": "2"},
                   {"content_type": "text", "title": "😭", "payload": "1"}]}

    params = {'recipient': recipient, 'message': message}
    data = json.dumps(params)
    headers = {'Content-Type': 'application/json'}  # json pattern

    response = http.request('POST', apiUrl, body=data, headers=headers)
    print(response.status)  # successful，200 is successful


def push_success(id):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    apiUrl = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAE358wDWxQBANcfxlUa3tfs7DPhsrrtJN8Q8AWvE7tvq3RdErlFyfHDKY8SMZBHR4YTK8fJkxW054ZAKDDfgXVkXzb0VPvj9gg2ZBs7rBI8k6Yt263vaxGMlBmsxks5oWfkiT7w2Uh5LiCeAll3lYfvpT7oFedMTiHaQMp7l60yVjJvhZAc'
    recipient = {'id': id}
    message = {
        "text": "Congratulations! registration is successful, please wait for the administrator to assign you to teams 😁"}

    params = {'recipient': recipient, 'message': message}
    data = json.dumps(params)
    headers = {'Content-Type': 'application/json'}  # json pattern

    response = http.request('POST', apiUrl, body=data, headers=headers)
    print(response.status)  # successful，200 is successful


def push_register(id):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    apiUrl = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAE358wDWxQBANcfxlUa3tfs7DPhsrrtJN8Q8AWvE7tvq3RdErlFyfHDKY8SMZBHR4YTK8fJkxW054ZAKDDfgXVkXzb0VPvj9gg2ZBs7rBI8k6Yt263vaxGMlBmsxks5oWfkiT7w2Uh5LiCeAll3lYfvpT7oFedMTiHaQMp7l60yVjJvhZAc'
    recipient = {'id': id}
    message = {
        'attachment': {'type': 'template',
                       'payload': {'template_type': 'button', 'text': 'Click here to register 😁',
                                   'buttons': [{
                                       "type": "web_url",
                                       "url": "https://mymood-service.herokuapp.com/register_messenger/" + id + "/",
                                       "title": "Click the here to register 👇",
                                       "webview_height_ratio": "full",
                                       "messenger_extensions": "true",
                                   }]}}}
    params = {'recipient': recipient, 'message': message}
    data = json.dumps(params)
    headers = {'Content-Type': 'application/json'}  # json pattern

    response = http.request('POST', apiUrl, body=data, headers=headers)
    print(response.status)


def keep_live():
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    apiUrl = 'https://messenger-mywebhook.herokuapp.com/webhook?hub.verify_token=EAAE358wDWxQBANcfxlUa3tfs7DPhsrrtJN8Q8AWvE7tvq3RdErlFyfHDKY8SMZBHR4YTK8fJkxW054ZAKDDfgXVkXzb0VPvj9gg2ZBs7rBI8k6Yt263vaxGMlBmsxks5oWfkiT7w2Uh5LiCeAll3lYfvpT7oFedMTiHaQMp7l60yVjJvhZAc&hub.mode=subscribe'
    response = http.request('GET', apiUrl)
    print("------Continuous activation service------" + str(response.status))  # successful，200 is successful


# a = '18:00'
# b = '17:35:39.586544'
# c = '08:00'
#
# print(a>b>c)
# an long
# keep_live()
# push_notifications("2334765856551775")
# push_notifications_team("2334765856551775")
# # xiao ming
# push_notifications("1823636781087934")
# # Karen
# push_notifications("1908572825896416")

# # Song di
# push_notifications("2281321371940745")

# push_notifications("1936024143139911")
