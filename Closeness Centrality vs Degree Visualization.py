import matplotlib.pyplot as plt
import numpy as np

degree = [1, 1, 1, 1, 1, 2, 2, 2, 3, 10, 11, 12, 15, 17, 25]
closeness = [0.09, 0.19, 0.22, 0.22, 0.22, 0.3, 0.33, 0.24, 0.34, 0.2, 0.24, 0.27, 0.29, 0.28, 0.38]

plt.figure(figsize=(10, 6), dpi=100)
plt.style.use('seaborn-v0_8-whitegrid')

scatter = plt.scatter(degree, closeness, c=closeness, cmap='plasma', 
                      s=150, alpha=0.9, edgecolors='black', linewidth=1.2)

cbar = plt.colorbar(scatter)
cbar.set_label('Closeness Intensity', fontsize=12, fontweight='bold')

plt.title('(A) Closeness Centrality vs Degree Visualization', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Degree', fontsize=12, fontweight='bold')
plt.ylabel('Closeness Centrality', fontsize=12, fontweight='bold')

plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

plt.show()
