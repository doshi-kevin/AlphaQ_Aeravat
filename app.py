import os
import streamlit as st
from moviepy.editor import *

# Function to extract audio from video buffer and save it as WAV format
def extract_audio(video_file, audio_name):
    try:
        # Save video buffer to a temporary file
        temp_video_path = "temp_video.mp4"
        with open(temp_video_path, "wb") as f:
            f.write(video_file.read())
        
        # Extract audio from the temporary video file
        video = VideoFileClip(temp_video_path)
        audio = video.audio
        audio_path = os.path.join('audio', audio_name + '.wav')
        audio.write_audiofile(audio_path, codec='pcm_s16le')
        
        # Close the video file
        video.close()
        
        # Remove the temporary video file
        os.remove(temp_video_path)
        
        return audio_path
    except Exception as e:
        st.error(f"Error occurred: {e}")

# Streamlit UI
st.title("Video to Audio Converter")

# Upload video file
video_file = st.file_uploader("Upload Video", type=["mp4"])

if video_file is not None:
    st.write("Video uploaded successfully!")

    audio_name = st.text_input("Enter Audio File Name:")

    if st.button("Extract Audio"):
        if audio_name.strip() == "":
            st.warning("Please enter a valid audio file name.")
        else:
            audio_path = extract_audio(video_file, audio_name)
            if audio_path:
                st.success("Audio extraction successful.")
                st.audio(audio_path, format='audio/wav', label='Extracted Audio')

                # Download link for the extracted audio
                st.markdown(f"### [Download Audio](/{audio_path})")
