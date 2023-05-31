import numpy as np
import sounddevice as sd

def play_sine_wave(frequency, duration, amplitude=0.3, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration))
    signal = amplitude * np.sin(2 * np.pi * frequency * t)

    sd.play(signal, sample_rate)
    sd.wait()

def map_to_sine_wave(char):
    frequencies = {
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
        'Y': 4698.63,
        'Z': 5274.04,
        '0': 440.0,
        '1': 493.88,
        '2': 523.25,
        '3': 587.33,
        '4': 659.25,
        '5': 698.46,
        '6': 783.99,
        '7': 880.0,
        '8': 987.77,
        '9': 1046.5
    }

    frequency = frequencies.get(char.upper(), 0.0)
    duration = 1.0  # Duration of the sine wave in seconds
    sampling_rate = 44100  # Number of samples per second

    t = np.linspace(0, duration, int(duration * sampling_rate))
    signal = np.sin(2 * np.pi * frequency * t)

    return signal

# Example usage
characters = "SsHh7RrIi8Gg6UuRrUuCc2Hh7Aa0RrAa0NnAa0SsAa0RrOoJj9Aa0RrAa0Jj9Aa0NnIi8Jj9Aa0MmAa0NnUuMmUuKkUuRrUuSsUuDd3Hh7Aa0RrIi8Bb1Aa0RrAa0NnAa0UuMmRrAa0Gg6Hh7UuBb1Aa0RrAa0Bb1Ii8MmAa0LlAa0Jj9Aa0SsUuJj9OoDd3Aa0YyAa0KkUuPpHh7Aa0LlAa0Cc2Hh7Aa0RrIi8Bb1UuDd3Dd3Hh7Ii8Hh7Ii8NnAa0TtAa0NnUuJj9Aa0NnIi8KkEe4SsUuMmIi8RrAa0UuMmPpAa0VvAa0NnAa0KkUuMmAa0RrAa0Bb1Aa0LlAa0Bb1UuDd3Dd3Hh7Ii8Bb1Ii8Dd3YyAa0Dd3Ee4Hh7UuMmOoHh7Ii8MmHh7Aa0RrAa0Hh7UuKkAa0LlEe4SsAa0Bb1Ii8KkAa0RrAa0"

duration = 1.0  # Duration of each sine wave in seconds
# Define the sampling rate and tempo
sampling_rate = 44100
tempo = 120  # BPM


for char in characters:
    frequency = map_to_sine_wave(char)
    play_sine_wave(frequency, duration)
