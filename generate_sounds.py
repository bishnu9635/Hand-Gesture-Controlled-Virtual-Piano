import numpy as np
from scipy.io.wavfile import write
import os


folder = "sounds"

if not os.path.exists(folder):
    os.makedirs(folder)


notes = {
    "C":261.63,
    "D":293.66,
    "E":329.63,
    "F":349.23,
    "G":392.00,
    "A":440.00,
    "B":493.88,

    "C2":523.25,
    "D2":587.33,
    "E2":659.25,
    "F2":698.46,
    "G2":783.99,
    "A2":880.00,
    "B2":987.77
}


sample_rate = 44100
duration = 1


for name,freq in notes.items():

    t = np.linspace(
        0,
        duration,
        int(sample_rate*duration)
    )

    wave = (
        0.5*np.sin(2*np.pi*freq*t)
    )

    audio = np.int16(
        wave * 32767
    )

    write(
        f"{folder}/{name}.wav",
        sample_rate,
        audio
    )


print("Piano sounds generated successfully")