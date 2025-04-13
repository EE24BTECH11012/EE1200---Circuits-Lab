import numpy as np
import matplotlib.pyplot as plt

# Component values
C1_highpass, C2_highpass, C1_lowpass, C2_lowpass = 1e-6, 1e-6, 1e-6, 1e-6  # 100 nF
R1_highpass, R2_highpass, R1_lowpass, R2_lowpass = 150e3, 150e3, 150, 150  # 5 kΩ

# Frequency range (log scale)
frequencies = np.logspace(1e-6, 5, 1000)  # 10 Hz to 100 kHz
w = 2 * np.pi * frequencies  # Convert to angular frequency

# Band-pass filter magnitude response
def bandpass(w, C1_highpass, C2_highpass, C1_lowpass, C2_lowpass, R1_highpass, R2_highpass, R1_lowpass, R2_lowpass):
    magnitudeLowpass = 1 / np.sqrt((1 - (w ** 2) * C1_lowpass * C2_lowpass * R1_lowpass * R2_lowpass) ** 2
                                   + (w * C1_lowpass * (R1_lowpass + R2_lowpass)) ** 2)
    magnitudeHighpass = ((w ** 2) * C1_highpass * C2_highpass * R1_highpass * R2_highpass) / np.sqrt((1 - (w ** 2)
                    * C1_highpass * C2_highpass * R1_highpass * R2_highpass) ** 2 + (w * R2_highpass * (C1_highpass + C2_highpass)) ** 2)
    magnitude = magnitudeHighpass * magnitudeLowpass
    return 20 * np.log10(magnitude)  # Convert to dB scale

# Compute response
y_values = bandpass(w, C1_highpass, C2_highpass, C1_lowpass, C2_lowpass, R1_highpass, R2_highpass, R1_lowpass, R2_lowpass)

# Calculate -3 dB cutoff frequencies
fc_lowpass = 1 / (2 * np.pi * np.sqrt(C1_lowpass * C2_lowpass * R1_lowpass * R2_lowpass))
fc_highpass = 1 / (2 * np.pi * np.sqrt(C1_highpass * C2_highpass * R1_highpass * R2_highpass))
fc_center = np.sqrt(fc_lowpass * fc_highpass)
cutoff_level = -3  # -3 dB standard cutoff level

# Plot
plt.figure(figsize=(8, 5))
plt.semilogx(frequencies, y_values, label="Band-Pass Filter", color="b", linewidth=2)

# Read and plot experimental data
with open("bandpass.txt", "r") as file:
    lines = file.readlines()
    for i in range(len(lines) - 1):
        f, v = lines[i].split()
        f = float(f)
        v = float(v)
        plt.scatter(f, 20 * np.log10(v/1.041), color="orange")  # Correct dB conversion

# Customization
plt.xlabel("Frequency (Hz)", fontsize=12)
plt.ylabel("Magnitude (dB)", fontsize=12)
plt.title("Band-Pass Filter Frequency Response", fontsize=14)  # Correct title
plt.grid(which="both", linestyle="--", linewidth=0.5)
plt.axhline(cutoff_level, color="r", linestyle="--", linewidth=1, label="-3 dB Cutoff")
plt.axvline(fc_lowpass, color="g", linestyle="--", linewidth=1, label=f"Low Cutoff: {fc_lowpass:.1f} Hz")
plt.axvline(fc_highpass, color="purple", linestyle="--", linewidth=1, label=f"High Cutoff: {fc_highpass:.1f} Hz")
plt.axvline(fc_center, color="cyan", linestyle="--", linewidth=1, label=f"Center Frequency: {fc_center:.1f} Hz")
plt.legend(fontsize=10)
plt.savefig('Bandpass.png')
plt.show()

