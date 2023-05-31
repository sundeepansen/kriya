import sounddevice as sd
import numpy as np
import re
from indic_transliteration import sanscript


# Define the mapping between Sanskrit letters and frequencies
sanskrit_mapping = {
    'A': 261.63,  # C4
    'B': 293.66,  # D4
    'C': 329.63,  # E4
    'D': 349.23,  # F4
    'E': 392.00,  # G4
    'F': 440.00,  # A4
    'G': 493.88,  # B4
    'H': 523.25,  # C5
    'I': 587.33,  # D5
    'J': 659.25,  # E5
    'K': 698.46,  # F5
    'L': 783.99,  # G5
    'M': 880.00,  # A5
    'N': 987.77,  # B5
    'O': 1046.50,  # C6
    'P': 1174.66,  # D6
    'Q': 1318.51,  # E6
    'R': 1396.91,  # F6
    'S': 1567.98,  # G6
    'T': 1760.00,  # A6
    'U': 1975.53,  # B6
    'V': 2093.00,  # C7
    'W': 2349.32,  # D7
    'X': 2637.02,  # E7
    'Y': 2793.83,  # F7
    'Z': 3135.96,  # G7
    'a': 349.23,  # F4
    'b': 392.00,  # G4
    'c': 440.00,  # A4
    'd': 493.88,  # B4
    'e': 523.25,  # C5
    'f': 587.33,  # D5
    'g': 659.25,  # E5
    'h': 698.46,  # F5
    'i': 783.99,  # G5
    'j': 880.00,  # A5
    'k': 987.77,  # B5
    'l': 1046.50,  # C6
    'm': 1174.66,  # D6
    'n': 1318.51,  # E6
    'o': 1396.91,  # F6
    'p': 1567.98,  # G6
    'q': 1760.00,  # A6
    'r': 1975.53,  # B6
    's': 2093.00,  # C7
    't': 2349.32,  # D7
    'u': 2637.02,  # E7
    'v': 2793.83,  # F7
    'w': 3135.96,  # G7
    'x': 349.23,  # F4
    'y': 392.00,  # G4
    'z': 440.00   # A4
}


# Function to generate the soundwave based on Sanskrit text
def generate_soundwave(sanskrit_text, bpm=120, key='C', tuning=440):
    # Convert Sanskrit text to Devanagari script
    devanagari_text = sanscript.transliterate(sanskrit_text, sanscript.ITRANS, sanscript.DEVANAGARI)

    # Convert Devanagari script to Roman script
    roman_text = sanscript.transliterate(devanagari_text, sanscript.DEVANAGARI, sanscript.ITRANS)

    # Remove non-alphabetic characters
    roman_text = re.sub('[^A-Za-z]', '', roman_text)

    # Convert text to lowercase
    roman_text = roman_text.lower()

    # Convert Roman script to soundwave frequencies
    soundwave = []
    for char in roman_text:
        if char in sanskrit_mapping:
            frequency = sanskrit_mapping[char]
            frequency = frequency * (tuning / 440)  # Adjust frequency based on tuning
            soundwave.extend(0.5 * np.sin(2 * np.pi * frequency * np.arange(int(60 / bpm * 44100)) / 44100))

    return np.array(soundwave)


# Function to play the soundwave at the specified BPM
def play_soundwave(soundwave, bpm):
    sd.play(soundwave, samplerate=44100, blocking=True)


# Example usage
sanskrit_text = "jaya hanumAna j~nAna guna sAgara jaya kapIsa tihuM loka ujAgara rAmadUta atulita bala dhAmA aMjani putra pavanasuta nAmA"
bpm = 23.25
key = 'C#'
tuning = 440

soundwave = generate_soundwave(sanskrit_text, bpm, key, tuning)
play_soundwave(soundwave, bpm)
