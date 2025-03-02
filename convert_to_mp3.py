from moviepy import AudioFileClip
import os


def convert_webm_to_mp3(webm_file):
    """
    Convert a .webm file to .mp3 format

    Parameters:
    webm_file (str): Path to the .webm file
    """
    try:
        print(f"Converting {webm_file} to MP3...")

        # Create the output filename
        base_name = os.path.splitext(webm_file)[0]
        mp3_file = f"{base_name}.mp3"

        # Convert to MP3
        audio = AudioFileClip(webm_file)
        audio.write_audiofile(mp3_file)
        audio.close()

        print(f"Conversion completed! File saved as: {mp3_file}")

        # Optionally remove the original .webm file
        remove_original = input("Do you want to remove the original .webm file? (y/n): ").lower()
        if remove_original == 'y':
            os.remove(webm_file)
            print("Original .webm file removed.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Get the .webm file from the current directory
    current_dir = os.getcwd()
    webm_files = [f for f in os.listdir(current_dir) if f.endswith('.webm')]

    if not webm_files:
        print("No .webm files found in the current directory.")
    else:
        if len(webm_files) == 1:
            convert_webm_to_mp3(webm_files[0])
        else:
            print("Multiple .webm files found:")
            for i, file in enumerate(webm_files):
                print(f"{i + 1}. {file}")
            choice = int(input("Enter the number of the file to convert: ")) - 1
            convert_webm_to_mp3(webm_files[choice])