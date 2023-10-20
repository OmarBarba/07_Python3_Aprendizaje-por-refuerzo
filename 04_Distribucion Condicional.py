import numpy as np
import matplotlib.pyplot as plt

mu = 0  # Media
sigma = 1  # Desviación estándar

# Generar datos de una distribución normal
datos = np.random.normal(mu, sigma, 1000)

# Crear un histograma
plt.hist(datos, bins=30, density=True)
plt.xlabel("Valor")
plt.ylabel("Probabilidad")
plt.title("Distribución Normal")
plt.show()
