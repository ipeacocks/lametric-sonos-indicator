import soco

devices = soco.discover()
if devices:
    for device in devices:
        print(f"Found device: {device.player_name}")
else:
    print("No devices found")

speaker = list(devices)[0]

# Get current track information
current_track = speaker.get_current_track_info()
print(f"Now playing: {current_track}")

sonos = soco.discovery.any_soco()
status = sonos.get_current_transport_info()
# print(status)