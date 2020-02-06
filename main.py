import soco

import requests
import time

import settings

# sonos = soco.SoCo('192.168.1.86')
sonos = soco.discovery.any_soco()

while True:
    track = sonos.get_current_track_info()
    status = sonos.get_current_transport_info()

    artist = track['artist']
    title = track['title']

    if status['current_transport_state'] == 'PLAYING':
        api_url = "http://%s:8080/api/v2/device/notifications" % (settings.lametric_ip)
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        basicAuthCredentials = ('dev', settings.lametric_api_key)
        data = '{"model":{"frames":[{"icon":"19113","text":"%s - %s"}]}}' % (artist, title)
        response = requests.post(api_url,
                                 headers=headers,
                                 auth=basicAuthCredentials,
                                 data=data.encode('utf-8'))
    time.sleep(60)