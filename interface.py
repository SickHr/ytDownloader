import customtkinter as ctk
from ytdownloader import YTDownloader
import threading

WIDTH = 350
HEIGHT = 350

class Interface:
    def __init__(self):
        # Create the root window
        self.root = ctk.CTk()
        self.root.title("YouTube Downloader")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.resizable(False, False)


        # Create the widgets
        self.url_label = None
        self.url_entry = None
        self.download_button = None

        # Call the gadgets method
        self.gadgets()

    def gadgets(self):
        self.url_label = ctk.CTkLabel(self.root, text="YTDownloader ", font=("Arial", 20))
        self.url_label.place(x=100, y=10)

        self.url_entry = ctk.CTkEntry(self.root, placeholder_text="Enter your URL here", width=200)
        self.url_entry.place(x=70, y=50)

        self.download_button = ctk.CTkButton(self.root, text="Download", command=self.start_download_thread)
        self.download_button.place(x=100, y=100)

        self.loading_label = ctk.CTkLabel(self.root, text="Loading...", font=("Arial", 15))

    def start_download_thread(self):
        download_thread = threading.Thread(target=self.download_video)
        download_thread.start()

    def download_video(self):
        if self.url_entry.get() == "":
            return

        self.loading_label.place(x=100, y=150)
        yt_url = self.url_entry.get()
        downloader = YTDownloader(yt_url)
        self.loading_label.configure(text="Download completed!")
        self.root.after(5000, self.loading_label.place_forget)  # Wait 5 seconds before hiding the label


