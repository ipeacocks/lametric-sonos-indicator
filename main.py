import soco

import json
import requests
import time
import os

# import settings

class LaSo:
    def __init__(self, lametric_ip, lametric_user, lametric_api_key, sonos):
        self.lametric_ip = lametric_ip
        self.lametric_user = lametric_user
        self.lametric_api_key = lametric_api_key
        self.sonos = sonos

    def get_track(self):
        track = self.sonos.get_current_track_info()
        status = self.sonos.get_current_transport_info()
        return track, status

    def send_notification(self):
        track, status = self.get_track()

        if status['current_transport_state'] == 'PLAYING':

            artist = track['artist']
            title = track['title']

            api_url = "http://%s:8080/api/v2/device/notifications" % (self.lametric_ip)
            headers = {'Content-Type': 'application/json; charset=utf-8'}
            basicAuthCredentials = (self.lametric_user, self.lametric_api_key)
            data = '{"model":{"frames":[{"icon":"19113","text":"%s - %s"}]}}' % (artist, title)
            try:
                response = requests.post(api_url,
                                         headers=headers,
                                         auth=basicAuthCredentials,
                                         data=data.encode('utf-8'),
                                         timeout=3)
                # for debugging purpose
                print(f"{artist} - {title}")
            except requests.exceptions.RequestException as err:
                print ("OOps: Something Else", err)
            except requests.exceptions.HTTPError as errh:
                print ("Http Error:", errh)
            except requests.exceptions.ConnectionError as errc:
                print ("Error Connecting:", errc)
            except requests.exceptions.Timeout as errt:
                print ("Timeout Error:", errt)  

def main():
    # If you wish to show specific speaker song use its IP
    # sonos = soco.SoCo('192.168.1.86')
    sonos = soco.discovery.any_soco()
    laso = LaSo(os.environ["LAMETRIC_IP"],
                "dev",
                os.environ["LAMETRIC_API_KEY"],
                sonos)
    # if envar DELAY isn't set than it equals 60
    delay = os.getenv('DELAY', 60)
    # print(delay)

    while True:
        laso.get_track()
        laso.send_notification()
        time.sleep(int(delay))

if __name__ == "__main__":
    main()