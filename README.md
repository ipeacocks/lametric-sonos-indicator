# Lametric Sonos Indicator

<p align="center">
  <img width="550" src="image.gif" />
</p>

This indicator shows current song which Sonos plays on Lametric Clock. Script should be launched externally on some 3rd system (maybe like [Raspberry Pi](https://www.raspberrypi.org/)) in your local network. Unfortunately [official Lametric application](https://apps.lametric.com/apps/display_for_sonos/4961) is buggy and doesn't work correct at least for me. 

## Requirements

This panel is written on next libraries:

* [SoCo](https://github.com/SoCo/SoCo)
* Requests

## Traditional Installation

Clone code:
```
$ git clone git@github.com:ipeacocks/lametric-sonos-indicator.git
```
Simply create virtualenv:
```
$ cd lametric-sonos-indicator
$ python3 -m venv venv
```
Activate virtual env:
```
$ source venv/bin/activate
```
That's almost it. Use `requirments.txt` to setup all python dependencies:
```
$ pip install -r requirements.txt
```
Get and create env variables [LAMETRIC_IP and LAMETRIC_API_KEY](https://lametric-documentation.readthedocs.io/en/latest/guides/first-steps/first-local-notification.html#find-api-key):
```
$ export LAMETRIC_API_KEY="e56b92_lametric_long_api_string_c2a0c4"
$ export LAMETRIC_IP="192.168.1.25"
$ export DELAY=30
```
`DELAY` is a time in seconds how often to send notification to Lametric Time.

And then lauch:
```
$ python3 main.py
```

## Docker

Also it's possible to launch this indicator in docker, but you need to build this image by yourself:
```
# cd lametric-sonos-indicator # this clonned repository
# docker build -t lametric-sonos .

# docker run \
  -d \
  --name lametric-sonos \
  --net host \
  --env LAMETRIC_IP="192.168.1.25" \
  --env LAMETRIC_API_KEY="e56b92_lametric_long_api_string_c2a0c4" \
  --env DELAY=60 \
  --restart unless-stopped \
  lametric-sonos
```

That's it. Hope it would be useful for you.

**Links**: \
https://lametric-documentation.readthedocs.io/en/latest/index.html \
https://blog.aruehe.io/tag/lametric/ \
http://docs.python-soco.com/en/latest/
