 import matplotlib.pyplot as plt

degree = [1, 2, 2, 2, 3, 10, 11, 12, 15, 17, 25]
stress = [0, 1400, 1800, 3700, 4500, 1700, 2900, 2050, 4050, 2900, 7700]

plt.figure(figsize=(10, 6), facecolor='#f0f2f6')
ax = plt.gca()
ax.set_facecolor('#ffffff')


scatter = plt.scatter(degree, stress, c=stress, cmap='plasma', 
                      s=150, alpha=0.85, edgecolors='black', linewidth=1.2)

cbar = plt.colorbar(scatter)
cbar.set_label('Stress Level Intensity', fontsize=12, fontweight='bold')

plt.title('(C) Scatter Plot: Degree vs Stress', fontsize=18, fontweight='bold', color='#2c3e50', pad=20)
plt.xlabel('Degree (Unit)', fontsize=13, fontweight='bold')
plt.ylabel('Stress (Value)', fontsize=13, fontweight='bold')

plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
