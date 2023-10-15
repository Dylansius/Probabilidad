# Definir un conjunto de datos de ejemplo
datos = ["A", "B", "A", "C", "A", "B", "C", "A", "A", "B"]

# Definir el evento de interés
evento_interes = "A"

# Calcular la probabilidad a priori del evento de interés
# P(A) = (Número de veces que A ocurre) / (Número total de eventos)
probabilidad_a_priori = datos.count(evento_interes) / len(datos)

print(f"La probabilidad a priori de '{evento_interes}' es: {probabilidad_a_priori}")

