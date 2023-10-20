# Probabilidad a priori de A y B
probabilidad_A_priori = 0.3  # Probabilidad a priori de que ocurra A
probabilidad_B_priori = 0.4  # Probabilidad a priori de que ocurra B

# Probabilidad de B dado A
probabilidad_B_dado_A = 0.7  # Probabilidad de que ocurra B dado que A ha ocurrido

# Aplicación de la Regla de Bayes para calcular la probabilidad de A dado B
probabilidad_A_dado_B = (probabilidad_B_dado_A * probabilidad_A_priori) / probabilidad_B_priori

# Imprimimos el resultado
print(f"Probabilidad de A dado B: {probabilidad_A_dado_B:.2f}")
