import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqresp

def rc_transfer_function(R, C, f):
    """
    Compute the transfer function H(f) = Vout/Vin of two cascaded series RC circuits.
    """
    omega = 2 * np.pi * f  # Convert frequency to angular frequency
    H_single = 1 / (1 + 1j * omega * R * C)  # Transfer function of one RC stage
    H_cascaded = H_single * H_single * H_single  # Cascading two identical RC stages
    return H_cascaded

# Define circuit parameters
R = 1e4  # Resistance in ohms (1kΩ)
C = 1e-7  # Capacitance in farads (1µF)

# Frequency range
frequencies = np.logspace(1, 6, 1000)  # 10 Hz to 1 MHz (log scale)
H = rc_transfer_function(R, C, frequencies)

# Compute magnitude and phase
magnitude = 20 * np.log10(np.abs(H))  # Convert magnitude to dB
phase = np.angle(H, deg=True)  # Phase in degrees

# Input points for validation
freqvals = np.array([1e3, 1e4, 100, 10, 5, 500, 50])
magvals = np.array([4e-3, 0, 320e-3, 944e-3, 980e-3, 28e-3, 560e-3])
phasevals = np.array([380e-6, 20e-6, 7.3e-3, 6.4e-3, 5.6e-3, 985e-6, 3.8e-3])
freqvals_rad = []
for i in range(len(freqvals)) :
    freqvals_rad.append(freqvals[i] * 2 * np.pi) 
    phasevals[i] *= freqvals_rad[i]*180/np.pi

print(magvals[4])
print(phasevals)

# Plot Bode magnitude response
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.semilogx(frequencies, magnitude, 'b')
plt.scatter(freqvals, 20 * np.log10(magvals), color='red', label='Input Points')
for i, txt in enumerate(freqvals):
    plt.annotate(f'({txt}, {20 * np.log10(magvals[i]):.2f})', (freqvals[i], 20 * np.log10(magvals[i])), textcoords="offset points", xytext=(5,5), ha='left')
plt.title('Bode Plot of Cascaded Series RC Circuit')
plt.ylabel('Magnitude (dB)')
plt.legend()
plt.grid(which='both', linestyle='--', linewidth=0.5)

# Plot Bode phase response
plt.subplot(2, 1, 2)
plt.semilogx(frequencies, phase, 'r')
plt.scatter(freqvals, phasevals, color='red', label='Input Points')
for i, txt in enumerate(freqvals):
    plt.annotate(f'({txt}, {phasevals[i]:.2f})', (freqvals[i], phasevals[i]), textcoords="offset points", xytext=(5,5), ha='left')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (degrees)')
plt.legend()
plt.grid(which='both', linestyle='--', linewidth=0.5)

# Show plots
plt.tight_layout()
plt.show()

