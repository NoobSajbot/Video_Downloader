# Video Downloader

A Python script to download videos based on information provided in an Excel file ('input.xlsx'). This program supports YouTube and possibly other video sources.

---

## Features
- Downloads videos from YouTube and other platforms.
- Supports optional specification of folder and file name for each video.
- Automatically downloads the highest quality version of the video (requires FFmpeg).
- Handles missing folder or title gracefully by using default values:
  - Default folder: Current working directory.
  - Default title: Video's original title from the source platform.

---

## Input File Format
The script requires an Excel file named 'input.xlsx' with the following structure:

| Column Name | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| **URL**     | The link to the video (required).                                           |
| **Folder**  | The folder where the video should be saved (optional).                     |
| **Title**   | The name of the video file when downloaded (optional).                     |

### Example
An example 'input.xlsx' file with two videos is provided in the repository.

| URL                                          | Folder         | Title         |
|----------------------------------------------|----------------|---------------| 
| https://www.youtube.com/watch?v=okpwkeclMu8  | Test_1         | woman         |
| https://www.youtube.com/watch?v=WvhYuDvH17I  |                |               |

- In the first row:
  - The video will be saved in the 'Test_1' folder with the name 'woman'.
- In the second row:
  - The video will be saved in the current working directory with its default title.

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/Video_Downloader.git
   cd Video_Downloader

    Install the required Python dependencies:
    pip install -r requirements.txt

    Ensure FFmpeg is installed. The script will attempt to install it automatically if not already available.

Usage

    Prepare the input.xlsx file with the required video information.
    Run the script: python yt_downloader.py

Quality Settings

By default, the script downloads the highest quality version of the video. If you encounter issues with FFmpeg or prefer a lower quality, modify the quality_setting variable in the script:

    Set quality_setting = 1 for high quality (default).
    Set quality_setting = 0 for standard quality.

Disclaimer

This tool is intended for lawful use only. Users are responsible for ensuring that their use of this tool complies with all applicable laws and the terms of service of any platforms involved, including YouTube. The author assumes no responsibility for any misuse of this tool.
License

This project is licensed under the MIT License. See the LICENSE file for details.
Contributing

Contributions are welcome! If you'd like to improve this script, feel free to submit a pull request or open an issue.