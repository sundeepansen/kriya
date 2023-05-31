import sounddevice as sd
import numpy as np
import random
from indic_transliteration import sanscript

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

# Frequency mapping for Sanskrit letters
frequency_mapping = {
    'A': 440.0,
    'B': 493.88,
    'C': 523.25,
    'D': 587.33,
    'E': 659.25,
    'F': 698.46,
    'G': 783.99,
    'H': 880.0,
    'I': 987.77,
    'J': 1046.5,
    'K': 1174.66,
    'L': 1318.51,
    'M': 1396.91,
    'N': 1567.98,
    'O': 1760.0,
    'P': 1975.53,
    'Q': 2093.0,
    'R': 2349.32,
    'S': 2637.02,
    'T': 2793.83,
    'U': 3135.96,
    'V': 3520.0,
    'W': 3951.07,
    'X': 4186.01,
    'Y': 4698.64,
    'Z': 5274.04,
    'a': 440.0,
    'b': 493.88,
    'c': 523.25,
    'd': 587.33,
    'e': 659.25,
    'f': 698.46,
    'g': 783.99,
    'h': 880.0,
    'i': 987.77,
    'j': 1046.5,
    'k': 1174.66,
    'l': 1318.51,
    'm': 1396.91,
    'n': 1567.98,
    'o': 1760.0,
    'p': 1975.53,
    'q': 2093.0,
    'r': 2349.32,
    's': 2637.02,
    't': 2793.83,
    'u': 3135.96,
    'v': 3520.0,
    'w': 3951.07,
    'x': 4186.01,
    'y': 4698.64,
    'z': 5274.04,
    '0': 440.0,
    '1': 493.88,
    '2': 523.25,
    '3': 587.33,
    '4': 659.25,
    '5': 698.46,
    '6': 783.99,
    '7': 880.0,
    '8': 987.77,
    '9': 1046.5,
}

def play_soundwave(soundwave, bpm):
    sd.play(soundwave, int(44100 * 60 / bpm), blocking=True)

def encode_sanskrit_to_sound(sanskrit_text, bpm):
    soundwave = np.array([])
    for char in sanskrit_text:
        if char in frequency_mapping:
            frequency = frequency_mapping[char]
            duration = 1.0  # Default duration for each sound is 1 second
            sound = 0.5 * np.sin(2 * np.pi * frequency * np.arange(int(duration * 44100)) / 44100)
            soundwave = np.concatenate((soundwave, sound))
        elif char == ' ':
            pause_duration = 1.0  # Default duration for a pause is 1 second
            pause = np.zeros(int(pause_duration * 44100))
            soundwave = np.concatenate((soundwave, pause))
    play_soundwave(soundwave, bpm)

# Example usage
sanskrit_text = "shrIguru charana saroja raja nija manu mukuru sudhAri baranaUM raghubara bimala jasu jo dAyaku phala chAri buddhihIna tanu jAnike sumirauM pavana kumAra bala buddhi bidyA dehu mohiM harahu kalesa bikAra jaya hanumAna j~nAna guna sAgara jaya kapIsa tihuM loka ujAgara rAmadUta atulita bala dhAmA"
bpm = 15
print("Sanskrit Text:", sanskrit_text)
encode_sanskrit_to_sound(sanskrit_text, bpm)
