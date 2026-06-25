# Reachy Mini HA Voice 用户说明

Reachy Mini HA Voice 是运行在 Reachy Mini 机器人上的 Home Assistant 语音卫星应用。
它通过 ESPHome 自动发现接入 Home Assistant，使用本地 MicroWakeWord 进行唤醒词和 Stop 检测，
并保留面向机器人交互调教过的听、想、说、空闲呼吸、DOA 转向和姿态保持动作。

## Home Assistant 接入

1. 在 Reachy Mini 桌面应用中安装并启动本应用。
2. 在 Home Assistant 中进入 **设置 → 设备与服务**。
3. 接受自动发现的 ESPHome 设备。
4. 如未自动发现，可手动添加 ESPHome：机器人 IP，端口 `6053`。

发现设备的元数据应为：

- 制造商：`Reachy Mini HA Voice`
- 型号：`Voice Satellite`
- 项目：`reachy-mini.ha-voice`

如果 Home Assistant 里已经有这个机器人的旧 ESPHome 设备，请先删除旧设备，再添加新发现的设备。

## 保留能力

- Okay Nabu、Hey Mycroft、Hey Jarvis 三个本地唤醒词
- TTS 和计时器播放期间可用的本地 Stop 词
- Home Assistant STT、对话、TTS、公告和计时器链路
- 听、想、说、唤醒、回正、空闲呼吸、情绪动作
- DOA 声源方向转向、手动头部 yaw 保持、姿态保持、身体 yaw 跟随
- 官方风格 60Hz 运动控制和 SDK 说话 wobble

## 视频

本应用不内置机器人侧视频推流。RTSP / 摄像头桥接继续由外部 Mac 视频桥负责。
