import numpy as np
import matplotlib.pyplot as plt

NUM = 100  # More points for a smoother plot
h = 0.0001
R = 1640
L = 1e-3
C = 1e-9
V0 = 5
omega = 1 / np.sqrt(L * C)
alpha = R / (2 * L)
omega_d = np.sqrt(omega**2 - alpha**2)  # Damped frequency

# Check underdamped condition
if C * R * R < 4 * L:
    print("Yes, proceed!")

# Time array
t = np.arange(0, NUM * h, h)

# Compute capacitor voltage
v_c = V0 * np.exp(-alpha * t) * (np.cos(omega_d * t) + (alpha / omega_d) * np.sin(omega_d * t))

# Compute current (derivative of capacitor voltage divided by capacitance)
i = -C * V0 * np.exp(-alpha * t) * (
    (-alpha * np.cos(omega_d * t) - omega_d * np.sin(omega_d * t)) +
    (alpha / omega_d) * (-alpha * np.sin(omega_d * t) + omega_d * np.cos(omega_d * t))
)

# Compute inductor voltage (L * di/dt)
v_l = L * np.gradient(i, h)

# Plot the results
plt.figure(figsize=(6, 6))
plt.plot(t, v_l)
plt.xlabel("Time (s)")
plt.ylabel("Inductor Voltage (V)")
plt.title("Voltage Across Inductor in RLC Circuit")
plt.grid(True)
plt.savefig('fig_inductor_voltage.png')
plt.show()

