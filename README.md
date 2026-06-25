---
title: Reachy Mini HA Voice
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: static
pinned: false
short_description: Reachy Mini voice companion for Home Assistant
tags:
  - reachy_mini
  - reachy_mini_python_app
  - reachy_mini_ha_voice
  - home_assistant
  - homeassistant
---

# Reachy Mini HA Voice

Reachy Mini HA Voice turns Reachy Mini into a Home Assistant voice satellite.
It runs on the robot, appears in Home Assistant through ESPHome auto-discovery,
keeps local wake/stop detection, and drives tuned Reachy Mini motion during
listening, thinking, speaking, idle breathing, and Home Assistant announcements.

## What It Does

- ESPHome auto-discovery on port `6053`
- Local MicroWakeWord detection for Okay Nabu, Hey Mycroft, Hey Jarvis, and Stop
- Home Assistant handles STT, conversation, TTS, timers, and announcements
- Stop word remains available during TTS and timer playback
- Motion states for listening, thinking, speaking, wake turns, idle breathing, emotions, and return-to-rest
- DOA sound-source turns, manual head yaw hold, posture hold, and body-yaw follow
- Official-style 60Hz motion loop and SDK speech wobbling
- No robot-side video service; RTSP/video stays outside this app

## Home Assistant Setup

1. Install and start the app on Reachy Mini.
2. In Home Assistant, open **Settings → Devices & Services**.
3. Accept the discovered ESPHome device.
4. If discovery does not appear, add ESPHome manually with the robot IP and port `6053`.

The discovered device metadata should be:

- Manufacturer: `Reachy Mini HA Voice`
- Model: `Voice Satellite`
- Project: `reachy-mini.ha-voice`

If Home Assistant already has an older ESPHome entry for this robot, remove that
old device first, then add the newly discovered one.

## Useful Entities

- Voice assistant satellite status
- Media player volume and mute
- Wake word slots and stop-word sensitivity
- DOA sound tracking and DOA angle
- Head/body/antenna pose controls
- Emotion selector
- Backend, daemon, control-loop, SDK, robot, Wi-Fi, and error diagnostics

Raw low-level entities such as individual IMU acceleration/gyro axes and head
X/Y/Z translation are intentionally hidden from the default Home Assistant view.

## Development

```bash
python -m compileall reachy_mini_ha_voice
python -m unittest discover -s tests
```

The project targets Python 3.12 and Reachy Mini SDK 1.8.3 or newer.
See [CHANGELOG.md](CHANGELOG.md) for release notes.
