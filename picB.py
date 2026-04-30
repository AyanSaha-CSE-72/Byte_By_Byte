import matplotlib.pyplot as plt
import numpy as np

degree = [1, 2, 2, 2, 3, 10, 11, 12, 15, 17, 25]
betweenness = [0.0, 0.1, 0.2, 0.41, 0.5, 0.195, 0.195, 0.23, 0.45, 0.33, 0.79]

plt.figure(figsize=(10, 6), facecolor='white')
plt.grid(True, linestyle='--', alpha=0.3)

scatter = plt.scatter(degree, betweenness, c=betweenness, cmap='turbo', 
                      s=180, alpha=0.9, edgecolors='black', linewidth=1.2)


cbar = plt.colorbar(scatter)
cbar.set_label('Betweenness Centrality Scale', fontsize=11, fontweight='bold')

plt.title('(B) Scatter Plot: Degree vs Betweenness Centrality', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Degree', fontsize=13, fontweight='bold')
plt.ylabel('Betweenness Centrality', fontsize=13, fontweight='bold')

plt.xlim(0, 28)
plt.ylim(-0.05, 0.9)
plt.tight_layout()

plt.show()
