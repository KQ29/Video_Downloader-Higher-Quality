import os
import logging
from yt_dlp import YoutubeDL
from config import DEFAULT_SAVE_PATH

def download_tiktok_video(url, save_path=DEFAULT_SAVE_PATH):
    ydl_opts = {
        'outtmpl': os.path.join(save_path, 'tiktok_%(id)s.%(ext)s'),
        'format': 'mp4',  # Only download mp4 format
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            logging.info(f"Downloading TikTok video from URL: {url}")
            ydl.download([url])
            logging.info("TikTok video downloaded successfully.")
    except Exception as e:
        logging.error(f"Error downloading TikTok video: {str(e)}")
