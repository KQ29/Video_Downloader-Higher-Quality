import os
import logging
from config import FFMPEG_PATH, DEFAULT_SAVE_PATH
from yt_dlp import YoutubeDL
from utils import reencode_video, check_quicktime_compatibility

def download_youtube_video(url, save_path=DEFAULT_SAVE_PATH):
    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'merge_output_format': 'mp4',
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            logging.info(f"Downloading YouTube video from URL: {url}")
            ydl.download([url])
            logging.info("YouTube video downloaded successfully.")
            
            downloaded_files = [f for f in os.listdir(save_path) if f.endswith(".mp4")]
            if downloaded_files:
                video_path = os.path.join(save_path, downloaded_files[0])
                output_path = os.path.join(save_path, "reencoded_" + os.path.basename(video_path))
                
                if not check_quicktime_compatibility(video_path):
                    logging.info("File is not compatible with QuickTime. Re-encoding...")
                    reencode_video(video_path, output_path)
    except Exception as e:
        logging.error(f"Error downloading YouTube video: {str(e)}")
