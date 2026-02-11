def predecir_futuro(hora, nivel_actual):
    es_pico = (7 <= hora <= 9) or (17 <= hora <= 19)

    if es_pico and nivel_actual >= 6:
        return "TENDENCIA: Alza severa (Saturación pronto)."
    elif es_pico:
        return "TENDENCIA: Incremento gradual por flujo laboral."
    else:
        return "TENDENCIA: Estable."
    
def obtener_recomendacion(nivel):
    if nivel >= 8:
        return "CRÍTICO: Desvío obligatorio."
    elif nivel >= 5:
        return "MODERADO: Avance con precaución."
    else:
        return "ÓPTIMO: Fluidez total."
    
def sugerir_mejor_opcion(avenida_solicitada):
    datos = sistema_vial.get(avenida_solicitada)
    
    if datos["nivel"] >= 7:
        return f"Usa la {datos['alterna']} para minimizar tu tiempo."
    else:
        return "Mantente en la ruta actual, es la más rápida."

sistema_vial = {
    "Av. Blanco Galindo": {"nivel": 8, "alterna": "Av. Capitán Victor Ustáriz"},
    "Av. América": {"nivel": 3, "alterna": "Calle Pantaleón Dalence"},
    "Av. Ayacucho": {"nivel": 9, "alterna": "Calle Punata"}
}

print("--- SISTEMA DE GESTIÓN DE TRÁFICO COCHABAMBA ---")

for avenida , datos in sistema_vial.items():
    print(f"\nAnalizando: {avenida}")

    nivel = datos["nivel"]

    prediccion = predecir_futuro(18, nivel)

    estado = obtener_recomendacion(nivel)

    print(f"[{estado}]")
    print(f"Predicción: {prediccion}")

if nivel >= 6:
        print(f" SUGERENCIA RACIONAL: {sugerir_mejor_opcion(avenida)}")

mejor_global = min(sistema_vial, key=lambda k: sistema_vial[k]['nivel'])
print(f"\n RUTA MÁS RÁPIDA EN LA CIUDAD AHORA: {mejor_global}")

