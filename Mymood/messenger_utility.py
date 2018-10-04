import requests
import urllib3
import json
import certifi


def push_notifications():
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    apiUrl = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAE358wDWxQBANcfxlUa3tfs7DPhsrrtJN8Q8AWvE7tvq3RdErlFyfHDKY8SMZBHR4YTK8fJkxW054ZAKDDfgXVkXzb0VPvj9gg2ZBs7rBI8k6Yt263vaxGMlBmsxks5oWfkiT7w2Uh5LiCeAll3lYfvpT7oFedMTiHaQMp7l60yVjJvhZAc'
    recipient = {'id': '2334765856551775'}
    # message = {'text': {'🤣', '😁', '😃','🙂','😐', '😔','😞', '😭','👿'}}
    # message = {'text': 'hello,world'}
    message = {'attachment': {'type': 'template', 'payload': {'template_type': 'button', 'text': 'Try the URL button!',
                                                              'buttons': [{
                                                                  "type": "web_url",
                                                                  "url": "https://mymood-service.herokuapp.com/select_emoji/",
                                                                  "title": "URL Button",
                                                                  "webview_height_ratio": "compact",
                                                                  "messenger_extensions": "true",
                                                                  # "fallback_url": "https://mymood-service.herokuapp.com/select_emoji/"
                                                              }]}}}
    # message = {"text": "how are you going?", "quick_replies": [
    #     {"content_type": "text", "title": "🤣", "payload": "0"},
    #     {"content_type": "text", "title": "😁", "payload": "1"},
    #     {"content_type": "text", "title": "😃", "payload": "2"},
    #     {"content_type": "text", "title": "🙂", "payload": "3"},
    #     {"content_type": "text", "title": "😐", "payload": "4"},
    #     {"content_type": "text", "title": "😔", "payload": "5"},
    #     {"content_type": "text", "title": "😞", "payload": "6"},
    #     {"content_type": "text", "title": "😭", "payload": "7"},
    #     {"content_type": "text", "title": "👿", "payload": "8"}]}

    params = {'recipient': recipient, 'message': message}
    data = json.dumps(params)
    headers = {'Content-Type': 'application/json'}  # json pattern

    response = http.request('POST', apiUrl, body=data, headers=headers)
    print(response.status)  # successful，200 is successful


push_notifications()
