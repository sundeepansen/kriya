from gtts import gTTS
import sounddevice as sd
import tempfile
import os


def convert_to_soundwaves(text):
    # Create a temporary file to save the audio
    temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)

    # Generate the audio file from the Sanskrit text
    tts = gTTS(text=text, lang="sa")
    tts.save(temp_file.name)

    # Load the audio file using sounddevice
    audio_data, fs = sd.read(temp_file.name)

    # Play the audio
    sd.play(audio_data, fs)
    sd.wait()


# Example usage
input_text = "नमो नारायणाय"
convert_to_soundwaves(input_text)
