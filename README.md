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

Reachy Mini HA Voice turns Reachy Mini into a Home Assistant voice companion.
It runs directly on the robot, exposes an ESPHome-compatible voice satellite,
keeps local wake/stop detection, and drives Reachy Mini motion so voice
interactions feel alive instead of static.

This is a clean project with its own package and app identity:

- Python distribution: `reachy-mini-ha-voice`
- Python package: `reachy_mini_ha_voice`
- Reachy Mini app entry point: `reachy_mini_ha_voice`
- Home Assistant device family: `Reachy Mini Voice`

## Highlights

- ESPHome auto-discovery for Home Assistant on port `6053`
- Local MicroWakeWord wake detection
- Wake words: Okay Nabu, Hey Mycroft, Hey Jarvis
- Local Stop word during TTS
- Home Assistant STT, conversation, and TTS pipeline integration
- Continuous conversation support
- DOA sound-source wake turns
- Tuned Reachy motion: listening, thinking, speaking, timers, emotions, idle breathing, antennas, and generated idle micro-actions
- Official-style 60Hz motion control and SDK speaking wobble
- Manual head yaw hold with body-yaw follow
- Curated Home Assistant entity surface

## Home Assistant Setup

1. Install and start the app on Reachy Mini.
2. In Home Assistant, open **Settings → Devices & Services**.
3. Accept the discovered ESPHome device, or add ESPHome manually.
4. If adding manually, use the robot IP address and port `6053`.

The discovered device should use metadata similar to:

- Manufacturer: `lichao622`
- Model: `Reachy Mini HA Voice`
- Project: `lichao622.Reachy Mini HA Voice`

If you previously used an older forked app, remove the old ESPHome device from
Home Assistant first, then add the newly discovered device.

## Home Assistant Entities

The app keeps the HA surface practical:

- Runtime controls: mute, speaker volume, idle behavior, continuous conversation
- Voice tuning: wake word slot 1, wake word slot 2, stop word sensitivity
- Motion controls: head roll, head pitch, head yaw, body yaw, left antenna, right antenna
- Sound direction: DOA angle, DOA sound tracking switch
- Diagnostics: daemon state, backend ready, control loop frequency, SDK version, robot name, wireless flag, simulation flag, WLAN IP, error message, IMU temperature
- Emotion selector: curated common emotion moves

Noisy low-level entities such as raw IMU acceleration/gyro axes, Head X/Y/Z
translation, Speech Detected, and Services Suspended are intentionally not
shown in Home Assistant.

## Motion Design

The motion system follows the current official Reachy Mini conversation style
where it matters:

- 60Hz control loop
- official-style idle breathing and antenna motion
- SDK-driven speaking wobble

It also preserves the custom behavior tuned for this project:

- generated idle micro-actions instead of a simple repeated loop
- DOA-based wake orientation
- smooth manual yaw hold
- body-yaw follow
- listening/thinking/speaking personality states
- delayed idle rest behavior when idle motion is disabled

## Voice Design

The voice pipeline follows the same broad shape as Linux Voice Assistant style
setups:

- local lightweight wake/stop detection
- Home Assistant handles STT, intent/conversation, and TTS
- Stop remains available during TTS
- sensitivity controls map to active wake-word slots

## Video

This app does not publish robot-side camera or RTSP video. Video is intentionally
kept outside the app and should be handled by the separate Mac RTSP bridge.

## Development

```bash
python -m compileall reachy_mini_ha_voice
python -m unittest discover -s tests
```

The project targets Python 3.12 and Reachy Mini SDK 1.8.3 or newer.

## Release

Version history starts at `1.1.0` for this clean project identity. See
[CHANGELOG.md](CHANGELOG.md).
