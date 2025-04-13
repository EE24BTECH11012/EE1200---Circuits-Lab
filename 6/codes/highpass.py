import numpy as np
import matplotlib.pyplot as plt

# Component values
C1, C2 = 1e-9, 1e-9  # 1 nF
R1, R2 = 15e3, 15e3  # 15 kΩ

# Frequency range (log scale)
frequencies = np.logspace(1, 5, 1000)  # 10 Hz to 100 kHz
w = 2 * np.pi * frequencies  # Convert to angular frequency

# High-pass filter magnitude response
def highpass(w, C1, C2, R1, R2):
    magnitude = ((w ** 2) * C1 * C2 * R1 * R2) / np.sqrt((1 - (w ** 2) * C1 * C2 * R1 * R2) ** 2 + (w * R2 * (C1 + C2)) ** 2)
    return 20 * np.log10(magnitude)  # Convert to dB scale

# Compute response
y_values = highpass(w, C1, C2, R1, R2)

# Calculate -3 dB cutoff frequency
fc = 1 / (2 * np.pi * np.sqrt(C1 * C2 * R1 * R2))
cutoff_level = -3  # -3 dB standard cutoff level

# Plot
plt.figure(figsize=(8, 5))
plt.semilogx(frequencies, y_values, label="High-Pass Filter", color="b", linewidth=2)

# Read and plot experimental data
with open("./highpass.txt", "r") as file:
    lines = file.readlines()
    for i in range(len(lines) - 1):
        f, v, dt = lines[i].split()
        f = float(f)
        v = float(v)
        if dt == "0":
            continue
        dt = float(dt) * (1e-6)
        
        plt.scatter(f, 20 * np.log10(v/2), color="orange")  # Correct dB conversion

# Customization
plt.xlabel("Frequency (Hz)", fontsize=12)
plt.ylabel("Magnitude (dB)", fontsize=12)
plt.title("High-Pass Filter Frequency Response", fontsize=14)
plt.grid(which="both", linestyle="--", linewidth=0.5)
plt.axhline(cutoff_level, color="r", linestyle="--", linewidth=1, label="-3 dB Cutoff")
plt.axvline(fc, color="g", linestyle="--", linewidth=1, label=f"Cutoff Frequency: {fc:.1f} Hz")
plt.legend(fontsize=10)
plt.savefig('Highpass.png')
plt.show()

