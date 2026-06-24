# Reachy Mini HA Voice - Project Summary

Reachy Mini HA Voice is a Home Assistant voice companion app for Reachy Mini.
It runs on the robot, exposes an ESPHome-compatible voice satellite, and keeps
the motion behavior we tuned for a more alive, less mechanical personality.

## Runtime Scope

- ESPHome protocol server on port 6053 with mDNS auto-discovery.
- Local MicroWakeWord detection for Okay Nabu, Hey Mycroft, Hey Jarvis, and Stop.
- Home Assistant pipeline for STT, conversation, TTS, timers, and media playback.
- Reachy Mini motion feedback for wake, listening, thinking, speaking, timers,
  emotions, idle breathing, generated idle micro-actions, and DOA wake turns.
- Manual head yaw hold, body-yaw follow, antenna controls, and curated emotion controls.

## Home Assistant Entity Surface

The project intentionally keeps the HA device page practical:

- Runtime controls: mute, speaker volume, idle behavior, continuous conversation.
- Voice tuning: wake word slot 1, wake word slot 2, and stop word sensitivity.
- Motion controls: head roll, pitch, yaw, body yaw, left antenna, right antenna.
- Sound direction: DOA angle and DOA sound tracking switch.
- Diagnostics: daemon state, backend ready, control loop frequency, SDK version,
  robot name, wireless flag, simulation flag, WLAN IP, error message, IMU temperature.
- Emotion selector: a curated set of useful emotion commands.

Raw IMU acceleration/gyro values, Head X/Y/Z translation controls, Speech Detected,
and Services Suspended are kept out of Home Assistant to reduce noise.

## Motion Policy

The app follows the current official Reachy Mini conversation style where it matters:

- 60Hz motion control cadence.
- Official-style idle breathing and antenna layer.
- SDK-driven speaking wobble.

It also keeps our custom behavior:

- Generated idle micro-actions instead of a simple fixed loop.
- DOA-based wake orientation.
- Smooth manual yaw hold and body-yaw follow.
- Listening/thinking/speaking personality states.

## Out Of Scope

Robot-side camera, vision AI, and RTSP publishing are not part of this app.
External video remains handled by the separate Mac RTSP bridge.
