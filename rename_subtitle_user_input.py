# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 19:48:41 2019

@author: Poe
This script sorts and renames all subtitle files
to match each TV serie episode names.
Simply copy & put the script in the same folder
with video & subtitle files, and execute.
"""

import os
dir_list = os.listdir()
sorted = sorted(dir_list)

#%%
sub_list = []
episode_list = []
video_ext = input("Enter video extension name without '.' (i.e. mkv): ")
dot_video_ext = "."+video_ext
for file in sorted:
    if file.endswith(".srt"):
        sub_list.append(file)
    elif file.endswith(dot_video_ext):
        episode_list.append(file)
    else:
        pass

#%%
renamed_sub = []
for file in episode_list:
    if file.endswith(dot_video_ext):
        renamed_sub.append(file.replace(dot_video_ext,".srt"))
    else:
        pass

#%%
for number in range(len(episode_list)):
    os.rename(sub_list[number],renamed_sub[number])
