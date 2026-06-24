# Reachy Mini HA Voice User Manual

## Installation

Install `reachy_mini_ha_voice` from the Reachy Mini app store. When started, it runs an ESPHome-compatible voice satellite on the robot.

Home Assistant should usually discover a new ESPHome device automatically:

- Name: `Reachy Mini Voice ******`
- Port: `6053`
- Manufacturer: `lichao622`
- Project: `lichao622.Reachy Mini HA Voice`

If discovery fails, add ESPHome manually in Home Assistant and enter the robot IP address with port `6053`.

## Voice

- Local MicroWakeWord wake words: Okay Nabu, Hey Mycroft, Hey Jarvis
- Local Stop word
- Home Assistant handles STT, conversation, and TTS
- Continuous conversation, mute, volume, wake sensitivity, and stop sensitivity are exposed in Home Assistant

## Motion

The app keeps the tuned motion system:

- Official-style 60Hz motion control
- Official idle breathing and antenna motion
- SDK speaking wobbling
- Listening, thinking, speaking, and timer motions
- Realtime generated idle micro-actions
- DOA sound-source wake turns
- Smooth manual Head Yaw hold
- Body Yaw follow for head and sound-source turns
- A curated set of useful emotion moves

## Home Assistant Entities

### Controls

| Entity | Type | Description |
| --- | --- | --- |
| Mute | Switch | Pause/resume the voice pipeline |
| Speaker Volume | Number | Speaker volume |
| Idle Behavior | Switch | Idle motion, breathing, antennas, and micro-actions |
| Continuous Conversation | Switch | Multi-turn conversation |
| Emotion | Select | Useful emotion moves |

### Voice Tuning

| Entity | Type | Description |
| --- | --- | --- |
| Wake Word 1 Sensitivity | Number | First active wake word threshold |
| Wake Word 2 Sensitivity | Number | Second active wake word threshold |
| Stop Word Sensitivity | Number | Stop word threshold |

### Motion Controls

| Entity | Type | Description |
| --- | --- | --- |
| Head Roll | Number | Head roll |
| Head Pitch | Number | Head pitch |
| Head Yaw | Number | Head yaw with hold behavior |
| Body Yaw | Number | Body yaw |
| Antenna L/R | Number | Left and right antennas |
| DOA Sound Tracking | Switch | Sound-source tracking |

### Diagnostics

| Entity | Type | Description |
| --- | --- | --- |
| Backend Ready | Binary Sensor | Backend availability |
| Daemon State | Text Sensor | Robot daemon state |
| DOA Angle | Sensor | Sound-source angle |
| Control Loop Frequency | Sensor | Motion loop frequency |
| SDK Version | Text Sensor | Reachy Mini SDK version |
| Robot Name | Text Sensor | Robot name |
| Wireless Version | Binary Sensor | Wi-Fi model flag |
| Simulation Mode | Binary Sensor | Simulation mode |
| WLAN IP | Text Sensor | Wireless IP |
| Error Message | Text Sensor | Current error |
| IMU Temperature | Sensor | IMU temperature |

## Out Of Scope

This app does not include robot-side camera, vision AI, or RTSP publishing. External video remains handled by the separate Mac RTSP bridge.
