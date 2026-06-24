# Reachy Mini HA Voice 用户手册

## 安装

从 Reachy Mini 应用商店安装 `reachy_mini_ha_voice`，启动后它会在机器人上开启 ESPHome 兼容的语音卫星服务。

Home Assistant 通常会自动发现新的 ESPHome 设备：

- 名称：`Reachy Mini Voice ******`
- 端口：`6053`
- 制造商：`lichao622`
- 项目：`lichao622.Reachy Mini HA Voice`

如果自动发现失败，可以在 Home Assistant 中手动添加 ESPHome，并填写机器人 IP 和端口 `6053`。

## 语音

- 本地 MicroWakeWord 唤醒词：Okay Nabu、Hey Mycroft、Hey Jarvis
- 本地 Stop 停止词
- STT、对话代理、TTS 由 Home Assistant 管线处理
- 支持连续对话、静音、音量、唤醒词灵敏度和 Stop 灵敏度

## 动作

应用保留调教后的动作系统：

- 官方风格 60Hz 运动控制
- 官方呼吸待机和天线动作
- SDK 说话 wobbling
- 聆听、思考、说话、计时器提醒动作
- 实时生成的空闲微动作
- DOA 声源方向唤醒转头
- 手动 Head Yaw 平滑保持
- Body Yaw 跟随头部/声源方向
- 精简但保留常用的情绪动作入口

## Home Assistant 实体

### 常用控制

| 实体 | 类型 | 说明 |
| --- | --- | --- |
| Mute | 开关 | 暂停/恢复语音链路 |
| Speaker Volume | 数值 | 扬声器音量 |
| Idle Behavior | 开关 | 空闲动作、呼吸、天线和微动作 |
| Continuous Conversation | 开关 | 连续对话 |
| Emotion | 选择器 | 常用情绪动作 |

### 语音调校

| 实体 | 类型 | 说明 |
| --- | --- | --- |
| Wake Word 1 Sensitivity | 数值 | 第一个启用唤醒词阈值 |
| Wake Word 2 Sensitivity | 数值 | 第二个启用唤醒词阈值 |
| Stop Word Sensitivity | 数值 | Stop 停止词阈值 |

### 姿态控制

| 实体 | 类型 | 说明 |
| --- | --- | --- |
| Head Roll | 数值 | 头部 Roll |
| Head Pitch | 数值 | 头部 Pitch |
| Head Yaw | 数值 | 头部 Yaw，支持保持 |
| Body Yaw | 数值 | 身体 Yaw |
| Antenna L/R | 数值 | 左右天线 |
| DOA Sound Tracking | 开关 | 声源方向追踪 |

### 诊断

| 实体 | 类型 | 说明 |
| --- | --- | --- |
| Backend Ready | 二进制传感器 | 后端是否可用 |
| Daemon State | 文本传感器 | daemon 状态 |
| DOA Angle | 传感器 | 声源方向 |
| Control Loop Frequency | 传感器 | 运动循环频率 |
| SDK Version | 文本传感器 | Reachy Mini SDK 版本 |
| Robot Name | 文本传感器 | 机器人名称 |
| Wireless Version | 二进制传感器 | Wi-Fi 版本标记 |
| Simulation Mode | 二进制传感器 | 仿真模式 |
| WLAN IP | 文本传感器 | 无线 IP |
| Error Message | 文本传感器 | 当前错误 |
| IMU Temperature | 传感器 | IMU 温度 |

## 不包含

这个应用不再包含机器人端摄像头、视觉 AI 或 RTSP 推流。视频流继续由 Mac 上单独的 RTSP 桥接服务负责。
