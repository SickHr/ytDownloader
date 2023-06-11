from pytube import YouTube
import os
import subprocess


class YTDownloader:
    # Initialize the class
    def __init__(self, download_path="C:/Users/blawa/Desktop/youtube_download"):
        self.link = None
        self.download_path = download_path

        get_url = input("Enter the URL of the video you want to download: ")
        self.link = get_url

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

        # Restart the program
        YTDownloader()



# Run the program
if __name__ == "__main__":
    YTDownloader()
