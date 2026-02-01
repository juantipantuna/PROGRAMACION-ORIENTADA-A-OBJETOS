"""
UNIVERSIDAD ESTATAL AMAZÓNICA
TAREA SEMANA 5 - TIPOS DE DATOS E IDENTIFICADORES
Estudiante: Juan Tipantuña
"""

# TIPOS DE DATOS PRIMITIVOS
nombre = "Juan Pérez"                     # String
edad = 22                                 # Integer
promedio = 8.75                           # Float
estudiante_activo = True                  # Boolean

# TIPOS DE DATOS COMPUESTOS
materias = ["Matemáticas", "Programación"]  # List
info_estudiante = {                        # Dictionary
    "nombre": nombre,
    "edad": edad,
    "promedio": promedio
}

# FUNCIONES CON IDENTIFICADORES DESCRIPTIVOS
def calcular_promedio(nota1, nota2, nota3):
    """Calcula el promedio de tres notas"""
    return (nota1 + nota2 + nota3) / 3

def verificar_aprobacion(promedio):
    """Verifica si el promedio es aprobatorio"""
    return promedio >= 7.0

# PROGRAMA PRINCIPAL
print("=" * 50)
print("SISTEMA ACADÉMICO - UEA")
print("=" * 50)

print(f"\nEstudiante: {nombre}")
print(f"Edad: {edad} años")
print(f"Promedio: {promedio}")

# Calcular nuevo promedio
nuevo_promedio = calcular_promedio(8.5, 9.0, 7.5)
print(f"\nPromedio semestral: {nuevo_promedio:.2f}")

# Verificar aprobación
if verificar_aprobacion(nuevo_promedio):
    print("Estado: APROBADO ✅")
else:
    print("Estado: REPROBADO ❌")

# Mostrar tipos de datos
print("\n" + "=" * 50)
print("TIPOS DE DATOS UTILIZADOS:")
print("=" * 50)
print(f"1. nombre -> {type(nombre)}")
print(f"2. edad -> {type(edad)}")
print(f"3. promedio -> {type(promedio)}")
print(f"4. estudiante_activo -> {type(estudiante_activo)}")
print(f"5. materias -> {type(materias)}")
print(f"6. info_estudiante -> {type(info_estudiante)}")

print("\n" + "=" * 50)
print("✅ TAREA COMPLETADA - SEMANA 5")
print("=" * 50)
