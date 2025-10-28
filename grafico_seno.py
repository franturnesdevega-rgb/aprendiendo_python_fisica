import numpy as np
import matplotlib.pyplot as plt

# Primer gráfico sencillo: una onda seno
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.figure(figsize=(6,4))
plt.plot(x, y, label='y = sin(x)', color='blue')
plt.title('Primera gráfica en Python')
plt.xlabel('x (radianes)')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
