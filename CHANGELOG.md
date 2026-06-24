# Changelog

All notable changes to Reachy Mini HA Voice are documented here.

## [1.1.0] - 2026-06-24

### Added
- Start the project as `reachy-mini-ha-voice` with the Python package `reachy_mini_ha_voice`.
- Provide ESPHome auto-discovery for Home Assistant on port 6053.
- Keep the tuned Reachy Mini motion system: official-style 60Hz control, breathing, antenna motion, generated idle micro-actions, listening/thinking/speaking states, emotion moves, DOA wake turns, manual head yaw hold, and body-yaw follow.
- Keep the OHF/Linux Voice inspired MicroWakeWord setup with Okay Nabu, Hey Mycroft, Hey Jarvis, and Stop.
- Keep Home Assistant voice pipeline integration for STT, conversation, TTS, media-player volume, mute, continuous conversation, and wake/stop sensitivity controls.

### Changed
- Rebrand Home Assistant device metadata to `Reachy Mini HA Voice` by `lichao622`.
- Trim the Home Assistant entity surface to the controls and diagnostics that are useful day to day.
- Keep internal robot capabilities available while removing noisy HA-facing entities such as Head X/Y/Z, raw IMU acceleration/gyro axes, Speech Detected, and Services Suspended.

### Removed
- Remove the old fork identity from package metadata, app entry point, README tags, and user-facing documentation.
- Remove robot-side video/camera features from the app scope; external RTSP remains handled by the separate Mac bridge.
