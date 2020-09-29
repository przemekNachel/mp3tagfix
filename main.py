import os
import taglib

for root, dirs, files in os.walk("D:\\mp3"):
    for file in files:
        if file.endswith(".mp3"):
            song = taglib.File(os.path.join(root, file))
            print(song.tags["ALBUM"])