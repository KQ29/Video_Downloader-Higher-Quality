# Video Downloader with Re-encoding

A Python-based video downloader that supports YouTube, TikTok, and Instagram. This tool uses `yt-dlp` and `instaloader` to download videos, with `ffmpeg` required for re-encoding to ensure QuickTime compatibility.

## Features

- Downloads videos from:
  - **YouTube**: Downloads the best available video and audio formats, merges them, and re-encodes if needed.
  - **TikTok**: Downloads videos in MP4 format.
  - **Instagram**: Supports downloading posts, reels, and profile content.
- Re-encodes videos using `ffmpeg` to H.264 (video) and AAC (audio) formats for maximum compatibility with QuickTime and other players.
  
## Requirements

- **Python 3.7+**
- **ffmpeg** (required for re-encoding to ensure compatibility)

### Installation

1. **Clone the repository**:
``` bash
   git clone https://github.com/yourusername/Video-Downloader-Recoding.git
   cd Video-Downloader-Recoding 
   ```
2. **Set up a virtual environment and install dependencies**:

``` bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
Install ffmpeg (required for re-encoding):

macOS:
bash
Copy code
brew install ffmpeg
Ubuntu/Debian:
bash
Copy code
sudo apt update
sudo apt install ffmpeg
Run the program:

bash
Copy code
python -m video_downloader
Enter the URL for the video (YouTube, TikTok, or Instagram) and, optionally, specify a save path (default is ./downloads).

Example Usage
plaintext
Copy code
Please provide the URL (YouTube, TikTok, or Instagram): https://youtu.be/sampleurl
Enter the save path or press Enter to use './downloads':
The program will download the video, re-encode it if necessary, and save it in the specified location.
Code Explanation
Re-encoding Requirement:

The downloader will download the best available video and audio formats separately if needed.
Using ffmpeg, the video is re-encoded to H.264 and AAC formats to ensure compatibility with most video players, including QuickTime.
Modular Design:

The code is organized into modules for each platform (YouTube, TikTok, Instagram) and utility functions, making it easy to maintain and expand.
Requirements:

A requirements.txt file is included for easy installation of dependencies. The ffmpeg installation is required for re-encoding functionality.
License
This project is licensed under the MIT License.

Additional Notes
Update the repository link (https://github.com/yourusername/Video-Downloader-Recoding.git) with your actual GitHub repository URL.
Be sure to have ffmpeg installed and accessible in your system path to enable re-encoding.
If you haven’t yet, generate a requirements.txt file by running:
bash
Copy code
pip freeze > requirements.txt