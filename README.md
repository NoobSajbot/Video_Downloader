# YouTube_Downloader
Script to download a set of youtube videos from information saved in the 'input.xlsx' file.

The file will include for each row information about the video as follows:
-the first column is the link to the youtube video
-the second column is the folder where the file should be saved
-the third column is the name of the video when downloaded.
An example with 2 videos is provided.

By default, the highest quality version of the file will be downloaded. This requires ffmpeg to be installed.
In case of problems, set the variable quality_setting to a value different from 1.

