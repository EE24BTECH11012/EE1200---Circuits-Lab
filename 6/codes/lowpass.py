import numpy as np
import matplotlib.pyplot as plt

# Component values
C1, C2 = 1e-9, 1e-9  # 100 nF
R1, R2 = 15e3, 15e3  # 5 kΩ

# Frequency range (log scale)
frequencies = np.logspace(1, 5, 1000)  # 10 Hz to 100 kHz
w = 2 * np.pi * frequencies  # Convert to angular frequency

# Low-pass filter magnitude response
def lowpass(w, C1, C2, R1, R2):
    magnitude = 1 / np.sqrt((1 - (w ** 2) * C1 * C2 * R1 * R2) ** 2 + (w * C1 * (R1 + R2)) ** 2)
    return 20 * np.log10(magnitude)  # Convert magnitude to dB

# Compute response
y_values = lowpass(w, C1, C2, R1, R2)
# Compute slope (derivative)
log_freq = np.log10(frequencies)
slope = np.gradient(y_values, log_freq)  # d(Magnitude in dB) / d(log10(frequency))
# Find roll-off slopes in stopband regions
low_freq_slope = np.mean(slope[:50])   # Approximate slope at low frequencies
high_freq_slope = np.mean(slope[-50:])  # Approximate slope at high frequencies
# Calculate -3 dB cutoff frequency
fc = 1 / (2 * np.pi * np.sqrt(C1 * C2 * R1 * R2))
cutoff_level = -3  # -3 dB standard cutoff level

# Plot
plt.figure(figsize=(8, 5))
plt.semilogx(frequencies, y_values, label="Low-Pass Filter", color="b", linewidth=2)

# Read and plot experimental data
with open("./lowpass.txt", "r") as file:
    lines = file.readlines()
    # lines.pop(0)
    for i in range(len(lines)-1) :
        f, v, dt = lines[i].split()
        f = float(f)
        v = float(v)
        if dt == "0":
            continue
        dt = float(dt) * (1e-6)
        
        plt.scatter(f, 20 * np.log10(v), color="orange")  # Convert voltage to dB

# Customization
plt.xlabel("Frequency (Hz)", fontsize=12)
plt.ylabel("Magnitude (dB)", fontsize=12)
plt.title("Low-Pass Filter Frequency Response", fontsize=14)
plt.grid(which="both", linestyle="--", linewidth=0.5)
plt.axhline(cutoff_level, color="r", linestyle="--", linewidth=1, label="-3 dB Cutoff")
plt.axvline(fc, color="g", linestyle="--", linewidth=1, label=f"Cutoff Frequency: {fc:.1f} Hz")
plt.legend(fontsize=10)
plt.savefig('Lowpass.png')
plt.show()

