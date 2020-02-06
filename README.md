# Lametric Sonos Indicator

<p align="center">
  <img width="550" src="image.gif" />
</p>

This indicator shows current song which Sonos plays on Lametric Clock. Script should be launched externally on some 3rd system (maybe like [Raspberry Pi](https://www.raspberrypi.org/)) in your local network. Unfortunately [official Lametric application](https://apps.lametric.com/apps/display_for_sonos/4961) is buggy and doesn't work correct at least for me. 

## Requirements

This panel is written on next libraries:

* [SoCo](https://github.com/SoCo/SoCo)
* Requests

## Installation

Clone code:
```
# git clone git@github.com:ipeacocks/lametric_sonos_indicator.git
```
Simply create virtualenv:
```
# cd lametric_sonos_indicator
# python3 -m venv venv
```
Activate virtual env:
```
# source venv/bin/activate
```
That's almost it. Use `requirments.txt` to setup all python dependencies:
```
# pip install -r requirements.txt
```
Rename `settings.py_example` to `settings.py`, fill IP of lametric there and launch:

```
python3 main_class.py
```
That's it. Hope it would be useful for you.