# =============================================
# PROGRAMA: Promedio Semanal del Clima (TRADICIONAL)
# Técnica: Programación Tradicional (Procedural)
# =============================================

def ingresar_temperaturas():
    """
    Solicita al usuario las temperaturas de los 7 días de la semana.
    Retorna una lista con los valores ingresados.
    """
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = []
    
    print("\n=== INGRESO DE TEMPERATURAS (TRADICIONAL) ===")
    print("Por favor, ingrese las temperaturas en grados Celsius:\n")
    
    for dia in dias:
        while True:
            try:
                temp = float(input(f"Temperatura del {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("¡Error! Debe ingresar un número válido.")
    
    return temperaturas

def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    """
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)

def mostrar_resultado(temperaturas, promedio):
    """
    Muestra las temperaturas ingresadas y el promedio calculado.
    """
    print("\n" + "="*50)
    print("RESULTADOS - PROGRAMACIÓN TRADICIONAL")
    print("="*50)
    
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    print("\n--- TEMPERATURAS SEMANALES ---")
    for i, dia in enumerate(dias):
        print(f"{dia:12}: {temperaturas[i]:6.1f}°C")
    
    print("\n" + "-"*50)
    print(f"PROMEDIO SEMANAL: {promedio:.2f}°C")
    
    # Clasificación del clima según el promedio
    if promedio < 10:
        clasificacion = "FRÍO"
    elif promedio < 25:
        clasificacion = "TEMPLADO"
    else:
        clasificacion = "CÁLIDO"
    
    print(f"CLASIFICACIÓN: {clasificacion}")
    print("="*50)

# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    print("="*60)
    print("SISTEMA DE CÁLCULO DE PROMEDIO SEMANAL DEL CLIMA")
    print("Versión: Programación Tradicional (Procedural)")
    print("="*60)
    
    # 1. Ingresar datos
    temps = ingresar_temperaturas()
    
    # 2. Calcular promedio
    prom = calcular_promedio(temps)
    
    # 3. Mostrar resultados
    mostrar_resultado(temps, prom)