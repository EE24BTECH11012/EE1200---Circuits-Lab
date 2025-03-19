import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Circuit parameters
R = 2948  # Resistance in ohms
L = 2.2e-3  # Inductance in Henry
C = 220e-9  # Capacitance in Farads

# Initial conditions
V0 = 5  # Initial voltage across the capacitor (in volts)
I0 = 0  # Initial current in the circuit (in amperes)

# Define the differential equation
def rlc_circuit(t, y):
    v, i = y
    dvdt = i / C
    didt = (-R * i - v) / L
    return [dvdt, didt]

# Time span for the simulation
t_span = (0, 0.01)  # Simulate from t=0 to t=1ms
t_eval = np.linspace(t_span[0], t_span[1], 1000000)  # Time points to evaluate the solution

# Solve the differential equation
sol = solve_ivp(rlc_circuit, t_span, [V0, I0], t_eval=t_eval)

# Extract the voltage across the capacitor
v_c = sol.y[0]

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(sol.t, v_c, label='Voltage across Capacitor (V)')
plt.title('Damping Oscillation Voltage in RLC Circuit')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.legend()
plt.show()
