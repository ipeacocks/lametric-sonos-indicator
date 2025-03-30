import soco

import json
import requests
import time
import os


class LaSo:
    def __init__(self, lametric_ip, lametric_user, lametric_api_key, sonos_devices):
        self.lametric_ip = lametric_ip
        self.lametric_user = lametric_user
        self.lametric_api_key = lametric_api_key
        self.sonos_devices = sonos_devices

    def get_track(self):
        print(self.sonos_devices)
        if not self.sonos_devices['Guest Room'].is_playing_tv and \
          self.sonos_devices['Guest Room'].get_current_transport_info()["current_transport_state"] == "PLAYING":
            soco_object = self.sonos_devices['Guest Room']
            if soco_object.get_current_track_info()["artist"] == '':
                soco_object = self.sonos_devices['Office Room']
            self.track = soco_object.get_current_track_info()
            self.status = soco_object.get_current_transport_info()
            self.is_playing_tv = soco_object.is_playing_tv
            # print(self.track, self.status, self.is_playing_tv)
            return self.track, self.status, self.is_playing_tv

    def send_notification(self):
        artist = self.track["artist"]
        title = self.track["title"]
        # print(artist)
        # print(title)

        api_url = "http://%s:8080/api/v2/device/notifications" % (self.lametric_ip)
        headers = {"Content-Type": "application/json; charset=utf-8"}
        basicAuthCredentials = (self.lametric_user, self.lametric_api_key)
        data = '{"model":{"frames":[{"icon":"19113","text":"%s - %s"}]}}' % (
            artist,
            title,
        )
        try:
            response = requests.post(
                api_url,
                headers=headers,
                auth=basicAuthCredentials,
                data=data.encode("utf-8"),
                timeout=3,
            )
            # for debugging purpose
            print(f"{artist} - {title}")
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)


def main():
    # if envar DELAY isn't set than it equals 60
    delay = os.getenv("DELAY", 60)

    while True:
        sonos_devices = {device.player_name: device for device in soco.discover()}
        laso = LaSo(os.environ["LAMETRIC_IP"], "dev", os.environ["LAMETRIC_API_KEY"], sonos_devices)
        if laso.get_track():
            laso.send_notification()
        time.sleep(int(delay))


if __name__ == "__main__":
    main()
