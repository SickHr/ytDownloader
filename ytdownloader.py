from pytube import YouTube
import os
import subprocess
import json


class YTDownloader:
    # Initialize the class
    def __init__(self, link):
        self.link = link
        self.download_path = json.load(open("config.json", "r"))["download_path"]


        yt = YouTube(self.link)

        # Get the highest resolution video-only stream
        video_stream = yt.streams.filter(only_video=True).order_by('resolution').desc().first()

        # Get the highest quality audio-only stream
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()


        # Print some information about the video
        print("Title: ", yt.title)
        print("Views: ", yt.views)
        print("Video Resolution: ", video_stream.resolution)


        # Download the video and audio streams
        video_filename = video_stream.download(output_path=self.download_path, filename="video")
        audio_filename = audio_stream.download(output_path=self.download_path, filename="audio")

        # Combine video and audio using FFmpeg and convert audio to AAC format
        output_file = os.path.join(self.download_path, f"{yt.title}.mp4")
        cmd = f'ffmpeg -i "{video_filename}" -i "{audio_filename}" -c:v copy -c:a aac "{output_file}"'
        subprocess.run(cmd, shell=True)

        # Optionally delete the separate video and audio files
        os.remove(video_filename)
        os.remove(audio_filename)

        print(f" " + "\n" * 20)
        print("Download and merge completed!")







