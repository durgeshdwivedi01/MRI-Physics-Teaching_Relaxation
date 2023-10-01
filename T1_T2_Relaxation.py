import matplotlib.pyplot as plt
import numpy as np

# Define T1 and T2 values (in seconds)
T1 = 1.0
T2 = 0.1

# Define time step and total simulation time (in seconds)
dt = 0.01
total_time = 5.0

# Initialize magnetization components
Mz = 1.0
Mxy = 0.0

# Create figure and axes for plotting
plt.figure(figsize=(10, 5))
plt.xlabel('Time (s)')
plt.ylabel('Magnetization')
plt.title('T1 Recovery and T2 Decay')

# Loop over time steps to update and plot magnetization components
times = np.arange(0, total_time, dt)
for t in times:
    if t == 0:
        Mxy = Mz
        Mz = 0.0
    
    # Update magnetization components based on T1 and T2 relaxation
    Mz += dt * (1 - Mz) / T1
    Mxy *= np.exp(-dt / T2)
    
    plt.scatter(t, Mz, color='b')  # T1 recovery (blue)
    plt.scatter(t, Mxy, color='r')  # T2 decay (red)

plt.legend(['Mz (T1 Recovery)', 'Mxy (T2 Decay)'])
plt.show()
