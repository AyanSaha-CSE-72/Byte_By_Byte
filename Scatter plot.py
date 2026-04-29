import matplotlib.pyplot as plt
import numpy as np


degree = [1, 2, 2, 2, 3, 10, 11, 12, 15, 17, 25]
stress = [0, 1600, 1800, 3700, 4500, 1700, 2900, 2100, 4050, 2900, 7700]


plt.figure(figsize=(10, 6))
plt.style.use('seaborn-v0_8-whitegrid')


scatter = plt.scatter(degree, stress, c=stress, cmap='coolwarm', 
                      s=100, alpha=0.8, edgecolors='w', linewidth=1)

plt.colorbar(scatter, label='Stress Intensity')


plt.title('Scatter plot', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Degree', fontsize=12, labelpad=10)
plt.ylabel('Stress', fontsize=12, labelpad=10)


plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
