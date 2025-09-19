# Windows Caption Logger

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Windows-10%2F11-blue)](https://www.microsoft.com/windows)
[![License](https://img.shields.io/badge/License-Private-red)](https://github.com/flap1/windows-caption-logger)

Real-time Windows Live Caption text capture and logging tool

## Features
- Automatic monitoring of Windows Live Captions
- Continuous text saving to `captions_log.txt`
- Real-time difference detection to prevent duplicates

## How to Launch Live Captions

### Method 1: Keyboard Shortcut
Press `Win + Ctrl + L` to toggle Live Captions on/off

### Method 2: Settings
1. Open Settings (`Win + I`)
2. Go to Accessibility → Captions
3. Turn on Live captions

### Method 3: Quick Settings
1. Press `Win + A` to open Quick Settings
2. Click on Accessibility
3. Toggle Live captions

## Usage
1. Launch Windows Live Captions using one of the methods above
2. Run the script: `uv run main.py`
3. Captions will be automatically saved to `captions_log.txt`

## Requirements
- Windows 10/11
- Python 3.8+
- uiautomation-win32

## Installation
```bash
git clone https://github.com/flap1/windows-caption-logger.git
cd windows-caption-logger
uv sync
```

## Run
```bash
uv run main.py
```