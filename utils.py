import subprocess
import logging
from config import FFMPEG_PATH

def reencode_video(input_path, output_path):
    try:
        subprocess.run([FFMPEG_PATH, "-i", input_path, "-c:v", "libx264", "-c:a", "aac", output_path], check=True)
        logging.info("Video re-encoded successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error re-encoding video: {e}")

def check_quicktime_compatibility(file_path):
    try:
        result = subprocess.run([FFMPEG_PATH, "-i", file_path], capture_output=True, text=True, check=True)
        return "Video: h264" in result.stderr and "Audio: aac" in result.stderr
    except subprocess.CalledProcessError:
        return False
