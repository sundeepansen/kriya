import numpy as np
import sounddevice as sd
import time

# Define the mapping of Sanskrit characters to frequency values
sanskrit_mapping = {
    'अ': 440, 'आ': 493.88, 'इ': 523.25, 'ई': 587.33, 'उ': 659.25, 'ऊ': 698.46, 'ऋ': 783.99, 'ए': 880,
    'ऐ': 932.33, 'ओ': 1046.5, 'औ': 1174.66, 'क': 261.63, 'ख': 293.66, 'ग': 329.63, 'घ': 349.23, 'ङ': 392,
    'च': 440, 'छ': 493.88, 'ज': 523.25, 'झ': 587.33, 'ञ': 659.25, 'ट': 698.46, 'ठ': 783.99, 'ड': 880,
    'ढ': 932.33, 'ण': 1046.5, 'त': 1174.66, 'थ': 261.63, 'द': 293.66, 'ध': 329.63, 'न': 349.23, 'प': 392,
    'फ': 440, 'ब': 493.88, 'भ': 523.25, 'म': 587.33, 'य': 659.25, 'र': 698.46, 'ल': 783.99, 'व': 880,
    'श': 932.33, 'ष': 1046.5, 'स': 1174.66, 'ह': 261.63, 'क्ष': 293.66, 'त्र': 329.63, 'ज्ञ': 349.23,
    '०': 0, '१': 1, '२': 2, '३': 3, '४': 4, '५': 5, '६': 6, '७': 7, '८': 8, '९': 9
}

# Define the sampling rate and tempo
sampling_rate = 44100
tempo = 120  # BPM

def generate_sine_wave(frequency, duration):
    # Generate a sine wave with the given frequency and duration
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    sine_wave = np.sin(2 * np.pi * frequency * t)
    return sine_wave

def play_sound(sine_wave):
    # Play the sound using sounddevice
    sd.play(sine_wave, sampling_rate)
    sd.wait()

def convert_sanskrit_to_sine_waves(sanskrit_text):
    # Calculate the duration of each note based on the tempo
    note_duration = 60 / tempo

    sine_waves = []
    for char in sanskrit_text:
        if char in sanskrit_mapping:
            frequency = sanskrit_mapping[char]
            if frequency != 0:
                sine_wave = generate_sine_wave(frequency, note_duration)
                sine_waves.append(sine_wave)

    # Combine all the sine waves into a single waveform
    combined_wave = np.concatenate(sine_waves)

    # Play the combined waveform
    play_sound(combined_wave)

# Example usage
input_text = "SsHh7RrIi8Gg6UuRrUuCc2Hh7Aa0RrAa0NnAa0SsAa0RrOoJj9Aa0RrAa0Jj9Aa0NnIi8Jj9Aa0MmAa0NnUuMmUuKkUuRrUuSsUuDd3Hh7Aa0RrIi8Bb1Aa0RrAa0NnAa0UuMmRrAa0Gg6Hh7UuBb1Aa0RrAa0Bb1Ii8MmAa0LlAa0Jj9Aa0SsUuJj9OoDd3Aa0YyAa0KkUuPpHh7Aa0LlAa0Cc2Hh7Aa0RrIi8Bb1UuDd3Dd3Hh7Ii8Hh7Ii8NnAa0TtAa0NnUuJj9Aa0NnIi8KkEe4SsUuMmIi8RrAa0UuMmPpAa0VvAa0NnAa0KkUuMmAa0RrAa0Bb1Aa0LlAa0Bb1UuDd3Dd3Hh7Ii8Bb1Ii8Dd3YyAa0Dd3Ee4Hh7UuMmOoHh7Ii8MmHh7Aa0RrAa0Hh7UuKkAa0LlEe4SsAa0Bb1Ii8KkAa0RrAa0"
convert_sanskrit_to_sine_waves(input_text)
