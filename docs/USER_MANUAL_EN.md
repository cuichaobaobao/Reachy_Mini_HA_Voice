# Reachy Mini HA Voice User Manual

Reachy Mini HA Voice is a Home Assistant voice satellite app that runs directly
on Reachy Mini. It connects through ESPHome auto-discovery, keeps local
MicroWakeWord wake/stop detection, and preserves the tuned robot motion used for
listening, thinking, speaking, idle breathing, DOA turns, and posture hold.

## Home Assistant Setup

1. Install and start the app from the Reachy Mini desktop application.
2. In Home Assistant, open **Settings → Devices & Services**.
3. Accept the discovered ESPHome device.
4. If discovery does not appear, add ESPHome manually with the robot IP and port `6053`.

The discovered device metadata should be:

- Manufacturer: `Reachy Mini HA Voice`
- Model: `Voice Satellite`
- Project: `reachy-mini.ha-voice`

If Home Assistant already has an older ESPHome entry for this robot, remove that
old device first, then add the newly discovered one.

## Preserved Features

- Okay Nabu, Hey Mycroft, and Hey Jarvis local wake words
- Local Stop word during TTS and timer playback
- Home Assistant STT, conversation, TTS, announcements, and timers
- Listening, thinking, speaking, wake, recenter, idle breathing, and emotion motion
- DOA sound-source turns, manual head yaw hold, posture hold, and body-yaw follow
- Official-style 60Hz motion control and SDK speech wobbling

## Video

This app does not include robot-side video streaming. RTSP/camera bridging stays
outside the app and is handled by the separate Mac video bridge.
