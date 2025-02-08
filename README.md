# YouTube Video Downloader 🎥📥

A simple and efficient Python script to download YouTube videos using `yt-dlp`. This tool is intended for educational and experimental purposes only. 📚🛠️

## Features 🚀

- Download YouTube videos in high quality.
- Supports multiple formats (MP4, M4A).
- Simple and easy-to-use command-line interface.
- Saves videos with appropriate titles.

## Installation 🖥️

### **Prerequisites**

Ensure you have the following installed:

- **Python** (3.7 or later)
- **yt-dlp** (Required for downloading videos)
- **ffmpeg** (Recommended for better output quality)

### **Setup**

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/YouTube-Video-Downloader.git
   cd YouTube-Video-Downloader
   ```
2. Install dependencies:
   ```bash
   pip install yt-dlp
   ```

## Configuration ⚙️

### **Updating Download Location**

By default, videos are saved in a user-defined folder. To change the location:

1. Open `downloader.py` in a text editor.
2. Modify the `output_path` variable to your desired folder location.
3. Save the file and rerun the script.

## Usage ▶️

1. Run the Python script:
   ```bash
   python downloader.py
   ```
2. Enter the YouTube video URL when prompted.
3. The video will be downloaded and saved in the specified folder.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer ⚠️

This tool is for educational purposes only. Downloading videos from YouTube without permission may violate their terms of service. The author is not responsible for any misuse of this tool.

---

### Optimized Script ✨

Here's an optimized version of your script with improved error handling and efficiency:

```python
import subprocess
import yt_dlp

def download_video(video_url, output_path):
    """
    Downloads a YouTube video using yt-dlp with better error handling.
    """
    try:
        command = f'yt-dlp -o "{output_path}/%(title)s.%(ext)s" {video_url} -S ext:mp4:m4a'
        subprocess.run(command, shell=True, check=True)
        print("✅ Download Completed!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_path = input("Enter the folder path to save the downloaded video: ")
    download_video(video_url, output_path)
```

This version:
- Improves error handling.
- Allows users to input the download folder dynamically.
- Ensures a smoother experience.

Let me know if you need any further refinements! 🚀

