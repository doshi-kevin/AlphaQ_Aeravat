import os
from moviepy.editor import *

def extract(video_path, audio_name):
    """
    Function that extracts audio from video and saves it as WAV format.
    """
    try:
        # Create the 'audio' folder if it doesn't exist
        if not os.path.exists('audio'):
            os.makedirs('audio')

        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(os.path.join('audio', audio_name + '.wav'), codec='pcm_s16le')
        print("Audio extraction successful.")
    except Exception as e:
        print("Error occurred:", e)

try:
    video_path = input('Video Path:\n'
                      + 'Example: C:\\Videos\\music.mp4\n')
    audio_name = input('\nAudio File Name:\n')

    extract(video_path, audio_name)

except Exception as e:
    print("Error occurred:", e)
