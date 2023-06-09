from pytube import YouTube
from sys import argv


link = argv[1]
yt = YouTube(link)
yd = yt.streams.get_highest_resolution()



print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length, "seconds")


download_path = "C:/Users/blawa/Desktop/youtube_download"

yd.download(download_path)

