# Probabilidad a priori
prior_probabilidad = 0.3

# Nueva evidencia
nueva_evidencia = 0.7

# Actualización de la probabilidad a priori con la Regla de Bayes
posterior_probabilidad = (prior_probabilidad * nueva_evidencia) / prior_probabilidad

print("Probabilidad posterior:", posterior_probabilidad)
