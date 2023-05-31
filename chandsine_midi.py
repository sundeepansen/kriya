import sounddevice as sd
import numpy as np
import re
import random
from indic_transliteration import sanscript
from midiutil import MIDIFile


# Mapping table for character to Chanda pattern
chanda_mapping = {
    'A': 'Ukta',
    'B': 'atyukta',
    'C': 'Madhya',
    'D': 'pratisTha',
    'E': 'suprstisTha',
    'F': 'gaayatri',
    'G': 'ushTikku',
    'H': 'anusThuppu',
    'I': 'bRhati',
    'J': 'paMkti',
    'K': 'trishTuppu',
    'L': 'jagati',
    'M': 'atijagati',
    'N': 'Sakvari',
    'O': 'atiSakvari',
    'P': 'ashTi',
    'Q': 'atyashTi',
    'R': 'dhRti',
    'S': 'atidhRti',
    'T': 'kRti',
    'U': 'prakRti',
    'V': 'aakRti',
    'W': 'vikRti',
    'X': 'sukRti',
    'Y': 'abhikRti',
    'Z': 'utkRti',
    'a': 'Ukta',
    'b': 'atyukta',
    'c': 'Madhya',
    'd': 'pratisTha',
    'e': 'suprstisTha',
    'f': 'gaayatri',
    'g': 'ushTikku',
    'h': 'anusThuppu',
    'i': 'bRhati',
    'j': 'paMkti',
    'k': 'trishTuppu',
    'l': 'jagati',
    'm': 'atijagati',
    'n': 'Sakvari',
    'o': 'atiSakvari',
    'p': 'ashTi',
    'q': 'atyashTi',
    'r': 'dhRti',
    's': 'atidhRti',
    't': 'kRti',
    'u': 'prakRti',
    'v': 'aakRti',
    'w': 'vikRti',
    'x': 'sukRti',
    'y': 'abhikRti',
    'z': 'utkRti',
    '0': 'Ukta',
    '1': 'atyukta',
    '2': 'Madhya',
    '3': 'pratisTha',
    '4': 'suprstisTha',
    '5': 'gaayatri',
    '6': 'ushTikku',
    '7': 'anusThuppu',
    '8': 'bRhati',
    '9': 'paMkti',
}

# Mapping table for Chanda pattern to frequency
chanda_frequency_mapping = {
    'Ukta': {'A': 261.63, 'a': 277.18, '0': 293.66},
    'atyukta': {'B': 311.13, 'b': 329.63, '1': 349.23},
    'Madhya': {'C': 369.99, 'c': 392.00, '2': 415.30},
    'pratisTha': {'D': 440.00, 'd': 466.16, '3': 493.88},
    'suprstisTha': {'E': 523.25, 'e': 554.37, '4': 587.33},
    'gaayatri': {'F': 587.33, 'f': 622.25, '5': 659.25},
    'ushTikku': {'G': 659.25, 'g': 698.46, '6': 739.99},
    'anusThuppu': {'H': 739.99, 'h': 783.99, '7': 830.61},
    'bRhati': {'I': 830.61, 'i': 880.00, '8': 932.33},
    'paMkti': {'J': 932.33, 'j': 987.77, '9': 1046.50},
}

# Function to generate the soundwave based on Sanskrit text and Chanda pattern
def generate_soundwave(sanskrit_text, chanda_text, bpm=120, key='C', tuning=440):
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
    for char, pattern in zip(roman_text, chanda_text.split()):
        if pattern in chanda_frequency_mapping:
            chanda_frequencies = chanda_frequency_mapping[pattern]
            if char in chanda_frequencies:
                frequency = chanda_frequencies[char]
                frequency = frequency * (tuning / 440)  # Adjust frequency based on tuning
                soundwave.extend(0.5 * np.sin(2 * np.pi * frequency * np.arange(int(60 / bpm * 44100)) / 44100))

    return np.array(soundwave)


# Function to generate a MIDI file from the soundwave
def generate_midi_file(soundwave, bpm, key, output_file):
    # Calculate the duration in seconds
    duration = len(soundwave) / 44100

    # Create a MIDI file with a single track
    midi_file = MIDIFile(1)
    track = 0

    # Set the tempo and key signature
    midi_file.addTrackName(track, 0, "Sanskrit Sound")
    midi_file.addTempo(track, 0, bpm)
    midi_file.addKeySignature(track, 0, key)

    # Convert soundwave to MIDI events
    for i, sample in enumerate(soundwave):
        velocity = int((sample + 1) * 127 / 2)  # Convert sample to velocity
        midi_file.addNote(
            track,
            0,
            i / 44100,  # Convert index to time in seconds
            i / 44100 + 1 / 44100,  # Set note duration as 1 sample
            random.randint(60, 80),  # Set random MIDI pitch (60-80)
            velocity,
            )

    # Save the MIDI file
    with open(output_file, 'wb') as file:
        midi_file.writeFile(file)


# Function to play the soundwave using sounddevice
def play_soundwave(soundwave, bpm):
    sd.play(soundwave, samplerate=44100, blocking=True)


# Example usage
sanskrit_text = "श्रीगुरु चरण सरोज रज निज मनु मुकुर सुधारि"
chanda_text = "Ukta atyukta Madhya pratisTha suprstisTha gaayatri"
bpm = 120
key = 'C'
tuning = 440

# Generate the soundwave
soundwave = generate_soundwave(sanskrit_text, chanda_text, bpm, key, tuning)

# Save the soundwave as a WAV file
output_file = "output.wav"
sd.write(output_file, soundwave, samplerate=44100)
sd.
# Generate a MIDI file from the soundwave
midi_file = "output.mid"
generate_midi_file(soundwave, bpm, key, midi_file)

# Play the soundwave
play_soundwave(soundwave, bpm)
