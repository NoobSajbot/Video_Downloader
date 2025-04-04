# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 17:24:34 2025

@author: Alberto Costa

#Download videos from link (YouTube, possibly other sources). 
Info in the 'input.xlsx' file, where for each row there are: video link [URL], destination folder [Folder], name of the destination file [Title]
"""

import os
import pandas as pd
from yt_dlp import YoutubeDL
import imageio_ffmpeg as ffmpeg


# Quality setting: 1 for high quality, use another value for low quality
quality_setting = 1


# Install FFmpeg automatically
def install_ffmpeg():
    ffmpeg_path = ffmpeg.get_ffmpeg_exe()
    print(f"FFmpeg installed at: {ffmpeg_path}")
    return ffmpeg_path


# Validate folder paths and create them if necessary
def validate_folder(folder):
    if not folder or pd.isna(folder):  # Use default folder if missing
        folder = os.getcwd()
    else:
        # Remove illegal characters for folder names
        invalid_chars = '<:"/\\|?*'
        folder = ''.join(c for c in folder if c not in invalid_chars)
        folder = folder.strip()  # Remove leading/trailing spaces
        if not folder:  # If folder becomes empty after cleaning
            folder = os.getcwd()
        os.makedirs(folder, exist_ok=True)  # Create folder if it doesn't exist
    return folder


# Download videos using yt-dlp
def download_videos(data, ffmpeg_path): 
    for _, row in zip(range(len(data)), data.iterrows()):        
        url = row[1]['URL']
        folder = validate_folder(row[1].get('Folder', None))
        title = row[1].get('Title', None)  # Use default title if missing
        if pd.isna(title):
            title=None

    # Define yt-dlp options
        ydl_opts = {
            'n_threads': 4,
            'prefer_free_formats': True,
            'ffmpeg_location': ffmpeg_path if quality_setting == 1 else None,
            'format': 'bestvideo+bestaudio/best' if quality_setting == 1 else 'best',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(folder, f'{title}.%(ext)s') if title else os.path.join(folder, '%(title)s.%(ext)s'),
        }

        try: 
            with YoutubeDL(ydl_opts) as ydl: 
                ydl.download([url])
        except Exception as e:
            print(f"Error downloading {url}: {e}")


def main():
    # Load data from Excel file
    try:
        data = pd.read_excel('input.xlsx')
    except FileNotFoundError:
        print("Error: 'input.xlsx' not found. Please ensure the file exists in the script's directory.")
        return

# Ensure required columns exist
    required_columns = ['URL', 'Folder', 'Title']
    for col in required_columns:
        if col not in data.columns:
            print(f"Error: Missing required column '{col}' in the Excel file.")
            return

# Install FFmpeg if needed
    ffmpeg_path = install_ffmpeg() if quality_setting == 1 else None

# Download videos
    download_videos(data, ffmpeg_path)


if __name__ == '__main__':
    main()