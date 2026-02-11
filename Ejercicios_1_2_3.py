"""Ejercicio 1"""
def analizar_trafico(flujo, umbral):
    # 1. Hora con mayor tráfico
    hora_pico = flujo.index(max(flujo))

    # 2. Promedio de vehículos por hora
    promedio = sum(flujo) / len(flujo)

    # 3. Horas donde el tráfico supera el umbral
    horas_sobre_umbral = []
    for i in range(len(flujo)):
        if flujo[i] > umbral:
            horas_sobre_umbral.append(i)

    return hora_pico, promedio, horas_sobre_umbral

flujo = [50, 120, 300, 450, 500, 480, 400, 350, 300, 200, 150, 100, 80, 60]
umbral = 300

hora_pico, promedio, horas_umbral = analizar_trafico(flujo, umbral)

print(f"Hora pico: {hora_pico} ({hora_pico + 6}:00)")
print(f"Promedio: {promedio:.2f}")
print(f"Horas sobre umbral: {horas_umbral}")

"""ejercicio 2"""

class Ruta:
    def __init__(self, nombre, distancia, tiempo_estimado, nivel_congestion):
        self.nombre = nombre
        self.distancia = distancia
        self.tiempo_estimado = tiempo_estimado
        self.nivel_congestion = nivel_congestion

    def indice_conveniencia(self):
        pesos = {
            "bajo": 3,
            "medio": 2,
            "alto": 1
        }

        peso = pesos.get(self.nivel_congestion.lower(), 1)
        return (peso * 10) / self.distancia

r1 = Ruta("Blanco Galindo", 5, 20, "alto")
r2 = Ruta("Alternativa 1", 6, 18, "medio")

rutas_por_avenida = {
    "Av. Principal": [r1, r2]
}

for ruta in rutas_por_avenida["Av. Principal"]:
    print(f"Ruta: {ruta.nombre}")
    print(f"Índice de conveniencia: {ruta.indice_conveniencia():.2f}\n")

"""ejercicio 3"""

def mejor_ruta(dic_rutas):
    penalizacion = {
        "bajo": 1,
        "medio": 2,
        "alto": 3
    }

    mejor = None
    mejor_puntaje = float("inf")

    for lista_rutas in dic_rutas.values():
        for ruta in lista_rutas:
            factor = penalizacion.get(ruta.nivel_congestion.lower(), 3)
            puntaje = ruta.tiempo_estimado * factor

            if puntaje < mejor_puntaje:
                mejor_puntaje = puntaje
                mejor = ruta

    return mejor

r1 = Ruta("Blanco Galindo", 5, 20, "alto")
r2 = Ruta("Alternativa 1", 6, 18, "medio")
r3 = Ruta("Ayacucho Directa", 4, 15, "bajo")

rutas = {
    "Av. América": [r1, r2],
    "Av. Ayacucho": [r3]
}

mejor = mejor_ruta(rutas)

print("Mejor ruta:")
print(mejor.nombre)
print(f"Tiempo: {mejor.tiempo_estimado} min")
print(f"Congestión: {mejor.nivel_congestion}")

