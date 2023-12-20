import yt_dlp
import subprocess

def download_video(video_url, output_path):
    # Constructing the command to download a video using yt-dlp
    # -o specifies the output template for the downloaded file
    # ext:mp4:m4a ensures that the downloaded file has an mp4 or m4a extension
    command = f'yt-dlp -o "{output_path}/%(title)s.%(ext)s" {video_url} -S ext:mp4:m4a'
    
    # Running the command using subprocess
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    # Taking user input for the YouTube video URL
    video_url = input("Enter the YouTube video URL: ")
    
    # Specifying the output path where the video will be downloaded
    output_path = "PUT THE FOLDER PATH WHERE YOU WANT TO SAVE THE DOWNLOADED VIDEOS"
    
    # Calling the download_video function
    download_video(video_url, output_path)
