# Datos de ejemplo: frecuencia de eventos A y B
eventos_A = 35  # Evento A ocurrió 35 veces
eventos_B = 20  # Evento B ocurrió 20 veces
total_eventos = 100  # Total de eventos en el conjunto de datos

# Calculamos la probabilidad condicionada de A dado B
probabilidad_A_dado_B = eventos_A / eventos_B

# Calculamos la probabilidad condicionada de no A dado B
probabilidad_no_A_dado_B = 1 - probabilidad_A_dado_B

# Normalizamos las probabilidades condicionadas para que sumen 1
probabilidad_total_dado_B = probabilidad_A_dado_B / (probabilidad_A_dado_B + probabilidad_no_A_dado_B)
probabilidad_no_A_dado_B = probabilidad_no_A_dado_B / (probabilidad_A_dado_B + probabilidad_no_A_dado_B)

# Imprimimos los resultados
print(f"Probabilidad de A dado B: {probabilidad_A_dado_B:.2f}")
print(f"Probabilidad de no A dado B: {probabilidad_no_A_dado_B:.2f}")
print(f"Probabilidad total dado B (normalizada): {probabilidad_total_dado_B:.2f}")
