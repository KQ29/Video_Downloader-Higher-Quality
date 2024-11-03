import logging
import instaloader
from config import DEFAULT_SAVE_PATH

def download_instagram_content(url, save_path=DEFAULT_SAVE_PATH):
    loader = instaloader.Instaloader(dirname_pattern=save_path)
    username = input("Enter your Instagram username (or press Enter to skip): ").strip()
    if username:
        password = input("Enter your Instagram password: ").strip()
        loader.login(username, password)

    try:
        if "/p/" in url or "/reel/" in url:
            shortcode = url.split("/")[-2]
            post = instaloader.Post.from_shortcode(loader.context, shortcode)
            loader.download_post(post, target=save_path)
            logging.info("Instagram post or reel downloaded successfully.")
        elif "/profile/" in url:
            profile_name = url.split("/")[-2]
            loader.download_profile(profile_name, profile_pic_only=False)
            logging.info(f"Instagram profile content downloaded for: {profile_name}")
        else:
            logging.error("Unsupported Instagram link format.")
    except Exception as e:
        logging.error(f"Error downloading Instagram content: {str(e)}")
