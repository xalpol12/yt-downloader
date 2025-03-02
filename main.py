import yt_dlp


def download_youtube_as_mp3(url, output_path=None):
    """
    Download a YouTube video as MP3 using yt-dlp

    Parameters:
    url (str): YouTube video URL
    output_path (str): Optional path to save the MP3 file. If not provided, saves in current directory.
    """
    # Configure yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s' if not output_path else f'{output_path}/%(title)s.%(ext)s',
        'verbose': False,
        'quiet': False,
        'no_warnings': True
    }

    try:
        print("Initializing download...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Get video info first
            info = ydl.extract_info(url, download=False)
            print(f"Downloading: {info['title']}")

            # Download the video
            ydl.download([url])

        print("Download completed successfully!")
        return True

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False


if __name__ == "__main__":
    # Example usage
    video_url = input("Enter YouTube URL: ")
    output_folder = input("Enter output folder (press Enter for current directory): ").strip()

    if not output_folder:
        output_folder = None

    download_youtube_as_mp3(video_url, output_folder)