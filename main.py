import os
import taglib

for root, dirs, files in os.walk("D:\\P\\Lamus\\mp3\\Albumy\\"):
    album = []
    for file in files:
        if file.endswith(".mp3"):
            song = taglib.File(os.path.join(root, file))
            alb = song.tags.get("ALBUM")
            if alb:
                album.extend(alb)
    album = list(set(album))
    if len(album) > 1:
        print(album)