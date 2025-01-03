"""
This is a simple program that generates notes from letters.

It will replace spaces and unknown characters with breaks.
"""
import numpy as np 
import sounddevice as sd 
import time as tm

string_to_notes = {"a":340,
                "b":350,
                "c":360,
                "d":370,
                "e":380,
                "f":390,
                "g":400,
                "h":410,
                "i":420,
                "j":430,
                "k":440,
                "l":470,
                "m":480,
                "n":490,
                "o":500,
                "p":510,
                "q":520,
                "r":530,
                "s":540,
                "t":550,
                "u":560,
                "v":570,
                "w":580,
                "x":590,
                "y":600,
                "z":610,
                " ":"break"}

string = str(input("Type what you want to convert to music notes here: "))
string = string.lower()

print(string)
notes = []

for word in string:
    for letter in word:
        
        if string_to_notes.get(letter) is not None:
            notes.append(string_to_notes[letter]) # this is a dict
            print(notes)
            
        else:
            notes.append(string_to_notes[" "])

print(notes)

for note in notes:
    
    if note == "break":
        tm.sleep(0.1)
        
    else:
        # Parameters for the sound
        frequency = note  # Frequency in Hz 
        duration = 0.1    # Duration in seconds
        sampling_rate = 44100  # Samples per second

        # Generate a sine wave
        time = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
        wave = 0.5 * np.sin(2 * np.pi * frequency * time)  # Amplitude scaled to 0.5

        # Play the sound
        sd.play(wave, samplerate=sampling_rate)
        sd.wait()  # Wait for the sound to finish
