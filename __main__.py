import os
from config import DEFAULT_SAVE_PATH
from youtube_downloader import download_youtube_video
from tiktok_downloader import download_tiktok_video
from instagram_downloader import download_instagram_content

def download_content_from_url(url, save_path=DEFAULT_SAVE_PATH):
    if "youtube.com" in url or "youtu.be" in url:
        download_youtube_video(url, save_path)
    elif "tiktok.com" in url:
        download_tiktok_video(url, save_path)
    elif "instagram.com" in url:
        download_instagram_content(url, save_path)
    else:
        print("Unsupported platform. Please provide a valid YouTube, TikTok, or Instagram URL.")

if __name__ == "__main__":
    url = input("Please provide the URL (YouTube, TikTok, or Instagram): ")
    save_path = input(f"Enter the save path or press Enter to use '{DEFAULT_SAVE_PATH}': ") or DEFAULT_SAVE_PATH
    os.makedirs(save_path, exist_ok=True)
    download_content_from_url(url, save_path)
