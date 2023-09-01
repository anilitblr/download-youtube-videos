from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import socket
import sys
import os

SAVE_DOWNLOADED_FILE = f"{os.getcwd()}/Downloads"


def check_internet_connection():
    remote_server = "www.youtube.com"
    port = 80
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        sock.connect((remote_server, port))
        return True
    except socket.error:
        return False
    finally:
        sock.close()


def Download(url):
    youtubeObject = YouTube(url)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        if youtubeObject is not None:
            print(f"Downloading: {youtubeObject.title}")
            # youtubeObject.streams.filter(progressive=True,
            # file_extension='mp4'
            # ).order_by('resolution').desc(
            # ).first().download(SAVE_DOWNLOADED_FILE, 'videoFilename', 'mp4')
            youtubeObject.download(SAVE_DOWNLOADED_FILE)
    except VideoUnavailable:
        print(f"Video {url} is unavailable, skipping.")
        sys.exit(1)
    print("Download is completed successfully.")


if check_internet_connection():
    pass
else:
    print("Internet is not connected.")
    sys.exit(1)

# checking if the directory Downloads exist or not.
if not os.path.exists(SAVE_DOWNLOADED_FILE):
    # if the Downloads directory is not present then create it.
    os.makedirs(SAVE_DOWNLOADED_FILE)


url = input("Enter the YouTube video URL: ")
if url.startswith("https://www.youtube.com"):
    Download(url)
else:
    print("ERROR: URL must start with https://www.youtube.com")
