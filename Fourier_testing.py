import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
from scipy.fft import rfft, rfftfreq, irfft

SAMPLE_RATE = 44100 #hz
DURATION = 162 # seconds

spf = wave.open("test_music.wav", "r")

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.frombuffer(signal, np.int16)

# If Stereo
if spf.getnchannels() == 2:
    print("Just mono files")
    sys.exit(0)
    
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.title("Signal Wave...")
plt.plot(signal)
plt.show()

# Number of samples in normalized_tone
N = SAMPLE_RATE * DURATION

plt.ticklabel_format(style='plain')
yf = rfft(signal)
xf = rfftfreq(N, 1 / SAMPLE_RATE)
plt.ylabel('Energy')
plt.xlabel('Frequency (hz)')
plt.plot(xf, np.abs(yf))
plt.show()

waves = np.array([np.array([])])

for i in range(44):
    individual_wave = irfft(np.abs(yf[0:100]))
    np.append(waves,individual_wave)