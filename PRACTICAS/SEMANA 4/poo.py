# =============================================
# PROGRAMA: Promedio Semanal del Clima (POO)
# Técnica: Programación Orientada a Objetos
# =============================================

class ClimaSemanal:
    """
    Clase que representa una semana de temperaturas.
    Encapsula los datos y operaciones relacionadas con el clima semanal.
    """
    
    # Atributo de clase (compartido por todas las instancias)
    DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    def __init__(self):
        """Inicializa una semana de clima con una lista vacía de temperaturas."""
        self.__temperaturas = []  # Atributo privado (encapsulado)
    
    def ingresar_temperaturas(self):
        """Solicita al usuario las temperaturas para cada día de la semana."""
        print("\n=== INGRESO DE TEMPERATURAS (POO) ===")
        print("Por favor, ingrese las temperaturas en grados Celsius:\n")
        
        for dia in self.DIAS_SEMANA:
            while True:
                try:
                    temp = float(input(f"Temperatura del {dia}: "))
                    self.__temperaturas.append(temp)
                    break
                except ValueError:
                    print("¡Error! Debe ingresar un número válido.")
    
    def calcular_promedio(self):
        """Calcula y retorna el promedio semanal de temperaturas."""
        if len(self.__temperaturas) == 0:
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)
    
    def clasificar_clima(self, promedio):
        """Clasifica el clima según el promedio semanal."""
        if promedio < 10:
            return "FRÍO"
        elif promedio < 25:
            return "TEMPLADO"
        else:
            return "CÁLIDO"
    
    def mostrar_resultados(self):
        """Muestra las temperaturas y el promedio calculado."""
        if len(self.__temperaturas) == 0:
            print("No hay temperaturas ingresadas.")
            return
        
        promedio = self.calcular_promedio()
        clasificacion = self.clasificar_clima(promedio)
        
        print("\n" + "="*50)
        print("RESULTADOS - PROGRAMACIÓN ORIENTADA A OBJETOS")
        print("="*50)
        
        print("\n--- TEMPERATURAS SEMANALES ---")
        for i, dia in enumerate(self.DIAS_SEMANA):
            print(f"{dia:12}: {self.__temperaturas[i]:6.1f}°C")
        
        print("\n" + "-"*50)
        print(f"PROMEDIO SEMANAL: {promedio:.2f}°C")
        print(f"CLASIFICACIÓN: {clasificacion}")
        print("="*50)
    
    # Método getter para acceder a las temperaturas (encapsulación)
    def get_temperaturas(self):
        return self.__temperaturas
    
    # Método setter para modificar temperaturas (encapsulación)
    def set_temperaturas(self, nuevas_temps):
        if len(nuevas_temps) == 7:
            self.__temperaturas = nuevas_temps
        else:
            print("Error: Debe proporcionar exactamente 7 temperaturas.")

# --- EJEMPLO DE HERENCIA (OPCIONAL) ---
class ClimaSemanalAvanzado(ClimaSemanal):
    """
    Clase derivada que extiende la funcionalidad de ClimaSemanal.
    Demuestra el concepto de HERENCIA en POO.
    """
    
    def calcular_max_min(self):
        """Calcula la temperatura máxima y mínima de la semana."""
        if len(self.get_temperaturas()) == 0:
            return None, None
        
        temps = self.get_temperaturas()
        max_temp = max(temps)
        min_temp = min(temps)
        
        return max_temp, min_temp
    
    def mostrar_analisis_completo(self):
        """Muestra un análisis completo del clima semanal."""
        self.mostrar_resultados()
        
        max_temp, min_temp = self.calcular_max_min()
        if max_temp is not None:
            print(f"\n--- ANÁLISIS AVANZADO ---")
            print(f"Temperatura MÁXIMA: {max_temp:.1f}°C")
            print(f"Temperatura MÍNIMA: {min_temp:.1f}°C")
            print(f"Rango térmico: {max_temp - min_temp:.1f}°C")

# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    print("="*60)
    print("SISTEMA DE CÁLCULO DE PROMEDIO SEMANAL DEL CLIMA")
    print("Versión: Programación Orientada a Objetos (POO)")
    print("="*60)
    
    # Versión básica (encapsulación)
    print("\n" + "="*60)
    print("IMPLEMENTACIÓN BÁSICA (ENCAPSULACIÓN)")
    print("="*60)
    
    clima_basico = ClimaSemanal()
    clima_basico.ingresar_temperaturas()
    clima_basico.mostrar_resultados()
    
    # Versión avanzada (herencia)
    print("\n\n" + "="*60)
    print("IMPLEMENTACIÓN AVANZADA (HERENCIA)")
    print("="*60)
    
    clima_avanzado = ClimaSemanalAvanzado()
    
    # Reutilizar las temperaturas ingresadas (ejemplo de polimorfismo)
    clima_avanzado.set_temperaturas(clima_basico.get_temperaturas())
    
    clima_avanzado.mostrar_analisis_completo()
    
    print("\n" + "="*60)
    print("PROGRAMA FINALIZADO")
    print("="*60)