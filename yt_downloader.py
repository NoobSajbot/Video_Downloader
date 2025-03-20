# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 2025

@author: Alberto Costa

#Download YoutTube videos. Info in the 'input.xlsx' file, where for each row there are: youtube link, destination folder, name of the destination file
"""

import pandas as pd
from yt_dlp import YoutubeDL
import imageio_ffmpeg as ffmpeg


# Quality setting: 1 for high quality. 
# Change to another value for low setting of if issues with ffmpeg
quality_setting = 1  


# Install FFmpeg automatically
def install_ffmpeg():
    ffmpeg_path = ffmpeg.get_ffmpeg_exe()
    print(f"FFmpeg installed at: {ffmpeg_path}")
    return ffmpeg_path

# Download videos using yt-dlp
def download_videos(urls, folders, titles, ffmpeg_path):
    for url, folder, title in zip(urls, folders, titles):
        if quality_setting==1:
            ydl_opts = {
                'n_threads': 4,
                'prefer_free_formats': True,  # Avoid authentication
                'ffmpeg_location': ffmpeg_path,
                'format': 'bestvideo+bestaudio/best',  # High-quality video and audio
                'merge_output_format': 'mp4',
                'outtmpl': f'{folder}/{title}.%(ext)s',  # Save in the specified folder with the specified name
            }
        else:
            ydl_opts = {
                'n_threads': 4,
                'prefer_free_formats': True,  # Avoid authentication
                'outtmpl': f'{folder}/{title}.%(ext)s',  # Save in the specified folder with the specified name
            }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

def main():
    # Load data from Excel file
    data = pd.read_excel('input.xlsx')
    urls = data.iloc[:, 0]
    titles = data.iloc[:, 2]
    
    #please avoid illegal folder names
    folders = [folder.replace(":", "-") for folder in data.iloc[:, 1]]

    if quality_setting==1:
    # Install FFmpeg
        ffmpeg_path = install_ffmpeg()
    
    # Download videos
        download_videos(urls, folders, titles, ffmpeg_path)
    else:
        # Download videos
            download_videos(urls, folders, titles, "")

if __name__ == '__main__':
    main()