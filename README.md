# Windows Caption Logger

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Windows-10%2F11-blue)](https://www.microsoft.com/windows)

Real-time Windows Live Caption text capture and logging tool for accessibility and transcription purposes.

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

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
- **flap1** - *Initial work*

## Acknowledgments
- Windows Accessibility team for Live Captions feature
- Python community for the excellent libraries