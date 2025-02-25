import numpy as np
import matplotlib.pyplot as plt

# Constants (example values, can be modified as needed)
A = 500000.0  # Area of the loop in m^2 (assumed value)
rho1 = 100000  # Resistivity of the first layer in ohm-m (assumed value)
eta = 0.1  # Noise level (assumed value)

# Function to calculate effective depth H
def calculate_depth(I, A, rho1, eta):
    M = I * A  # Magnetic moment
    H = 0.55 * (M * rho1 / eta) ** (1/5)  # Effective depth
    return H

# Range of currents (A to Amperes)
currents = np.linspace(0.1, 100, 100)  # from 0.1 A to 100 A

# Calculate depths for these currents
depths = [calculate_depth(I, A, rho1, eta) for I in currents]

# Plotting the result
plt.figure(figsize=(8, 6))
plt.plot(currents, depths, label="Depth vs Current", color="b")
plt.xlabel("Current (I) in Amperes")
plt.ylabel("Effective Depth (H) in meters")
plt.title("Effect of Current on Effective Depth in TEM Method")
plt.grid(True)
plt.legend()
plt.show()
