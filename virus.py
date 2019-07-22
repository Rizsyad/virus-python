import os
import fnmatch

path = '/host-rootfs/storage/' #change this dir you want

for dirpath, dirnames, filenames in os.walk(path):

    if not filenames:
        continue
        
    pythonic_files = fnmatch.filter(filenames, "*.jpeg") + fnmatch.filter(filenames, "*.jpg") + fnmatch.filter(filenames, "*.png") + fnmatch.filter(filenames, "*.gif") + fnmatch.filter(filenames, "*.bmp") + fnmatch.filter(filenames, "*.mp4") + fnmatch.filter(filenames, "*.3gp") + fnmatch.filter(filenames, "*.webm") + fnmatch.filter(filenames, "*.mkv") + fnmatch.filter(filenames, "*.flv") + fnmatch.filter(filenames, "*.ogg") + fnmatch.filter(filenames, "*.avi") + fnmatch.filter(filenames, "*.m4p") + fnmatch.filter(filenames, "*.m4v") + fnmatch.filter(filenames, "*.mp3") + fnmatch.filter(filenames, "*.m4a") + fnmatch.filter(filenames, "*.wav") + fnmatch.filter(filenames, "*.m4b") + fnmatch.filter(filenames, "*.flac")
    if pythonic_files:
        for file in pythonic_files:
            print('{}/{}'.format(dirpath, file))
            os.remove('{}/{}'.format(dirpath, file))
