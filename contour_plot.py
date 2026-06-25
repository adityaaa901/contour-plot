import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create grid data for contour plot
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Calculate Z values (example: Gaussian function)
Z = np.exp(-(X**2 + Y**2) / 2)

# Create contour plot
plt.figure(figsize=(10, 8))
contour = plt.contourf(X, Y, Z, levels=15, cmap='viridis')
contour_lines = plt.contour(X, Y, Z, levels=8, colors='black', linewidths=0.5, alpha=0.3)

# Add colorbar
cbar = plt.colorbar(contour, label='Z Values')
cbar.set_label('Z Values', fontweight='bold')

plt.xlabel('X', fontsize=12, fontweight='bold')
plt.ylabel('Y', fontsize=12, fontweight='bold')
plt.title('Contour Plot', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Display the plot
plt.show()
