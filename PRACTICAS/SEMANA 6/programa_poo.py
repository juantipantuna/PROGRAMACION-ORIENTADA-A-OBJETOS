# programa_poo.py
"""
===================================================
TAREA SEMANA 6 - PROGRAMACIÓN ORIENTADA A OBJETOS
===================================================
UNIVERSIDAD: Universidad Estatal Amazónica
ESTUDIANTE: Juan Tipantuna
CARRERA: Tecnología de la información
NIVEL: 2
CORREO: juantipantuna22@gmail.com
FECHA: 18 de enero del 2026
===================================================

CONCEPTOS DEMOSTRADOS:
✓ HERENCIA: Relación entre clase padre e hijas
✓ ENCAPSULACIÓN: Protección de datos con atributos privados
✓ POLIMORFISMO: Mismo método, diferentes comportamientos
===================================================
"""


# ======================
# 1. CLASE BASE - HERENCIA
# ======================
class Vehiculo:
    """
    Clase base que representa un vehículo genérico.
    Esta clase será heredada por Automovil y Motocicleta.
    """

    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        print(f"[CREACIÓN] Vehículo {marca} {modelo} ({año}) creado")

    def descripcion(self):
        """Retorna descripción completa del vehículo"""
        return f"{self.marca} {self.modelo} - Año {self.año}"

    def arrancar(self):
        """Método base que será sobrescrito (polimorfismo)"""
        return "Vehículo arrancando..."

    def mostrar_tipo(self):
        """Método que identifica el tipo de vehículo"""
        return "Vehículo genérico"


# ======================
# 2. CLASE DERIVADA 1 - HERENCIA + POLIMORFISMO
# ======================
class Automovil(Vehiculo):
    """
    Clase derivada que representa un automóvil.
    Hereda de Vehiculo y demuestra polimorfismo.
    """

    def __init__(self, marca, modelo, año, puertas, color="blanco"):
        # Llamada al constructor de la clase padre
        super().__init__(marca, modelo, año)
        self.puertas = puertas
        self.color = color
        print(f"[ESPECIFICACIÓN] Automóvil con {puertas} puertas, color {color}")

    # POLIMORFISMO: Sobrescritura del método arrancar
    def arrancar(self):
        return f"🚗 {self.marca} {self.modelo} arrancando... ¡Vroom Vroom!"

    def mostrar_tipo(self):
        return "Automóvil"

    def info_completa(self):
        return f"{self.descripcion()}, {self.puertas} puertas, Color: {self.color}"


# ======================
# 3. CLASE DERIVADA 2 - HERENCIA + POLIMORFISMO
# ======================
class Motocicleta(Vehiculo):
    """
    Otra clase derivada que representa una motocicleta.
    Demuestra que múltiples clases pueden heredar de la misma base.
    """

    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada
        print(f"[ESPECIFICACIÓN] Motocicleta {cilindrada}cc")

    # POLIMORFISMO: Sobrescritura diferente
    def arrancar(self):
        return f"🏍️ {self.marca} {self.modelo} encendida... ¡Brum Brum!"

    def mostrar_tipo(self):
        return "Motocicleta"

    def info_completa(self):
        return f"{self.descripcion()}, {self.cilindrada}cc"


# ======================
# 4. ENCAPSULACIÓN COMPLETA
# ======================
class CuentaBancaria:
    """
    Clase que demuestra encapsulación con atributos privados.
    Los datos están protegidos y solo se acceden mediante métodos.
    """

    def __init__(self, titular, numero_cuenta, saldo_inicial=0):
        self.titular = titular
        self.__numero_cuenta = numero_cuenta  # Privado
        self.__saldo = saldo_inicial  # Privado
        print(f"[CUENTA] Creada para {titular}, Saldo inicial: ${saldo_inicial}")

    # ===== GETTERS (acceso controlado) =====
    def get_saldo(self):
        """Obtiene el saldo actual (método getter)"""
        return self.__saldo

    def get_numero_cuenta(self):
        """Obtiene número de cuenta (método getter)"""
        # Podríamos mostrar solo parte por seguridad
        return f"****{str(self.__numero_cuenta)[-4:]}"

    # ===== SETTERS (modificación controlada) =====
    def depositar(self, monto):
        """Deposita dinero con validación (método setter)"""
        if monto > 0:
            self.__saldo += monto
            return f"✅ ${monto} depositado. Nuevo saldo: ${self.__saldo}"
        return "❌ Monto debe ser positivo"

    def retirar(self, monto):
        """Retira dinero con validación (método setter)"""
        if monto <= 0:
            return "❌ Monto debe ser mayor a cero"
        elif monto > self.__saldo:
            return f"❌ Fondos insuficientes. Saldo actual: ${self.__saldo}"
        else:
            self.__saldo -= monto
            return f"✅ ${monto} retirado. Nuevo saldo: ${self.__saldo}"

    def transferir(self, otra_cuenta, monto):
        """Transfiere a otra cuenta (operación compleja encapsulada)"""
        retiro = self.retirar(monto)
        if "✅" in retiro:
            otra_cuenta.depositar(monto)
            return f"✅ Transferencia de ${monto} realizada exitosamente"
        return retiro


# ======================
# 5. DEMOSTRACIÓN PRÁCTICA
# ======================
def main():
    """Función principal que demuestra todos los conceptos"""

    print("\n" + "=" * 70)
    print(" " * 20 + "📚 TAREA SEMANA 6 - POO")
    print(" " * 15 + "Juan Tipantuna - juantipantuna22@gmail.com")
    print("=" * 70)

    # === HERENCIA ===
    print("\n🔹 1. DEMOSTRACIÓN DE HERENCIA")
    print("-" * 40)

    auto = Automovil("Toyota", "Corolla", 2023, 4, "rojo")
    moto = Motocicleta("Yamaha", "YZF-R3", 2024, 321)

    print(f"\n• {auto.info_completa()}")
    print(f"• {moto.info_completa()}")
    print("✅ Ambas heredan de la clase Vehiculo")

    # === POLIMORFISMO ===
    print("\n\n🔹 2. DEMOSTRACIÓN DE POLIMORFISMO")
    print("-" * 40)
    print("Mismo método 'arrancar()', diferente comportamiento:")

    print(f"\n• {auto.mostrar_tipo()}: {auto.arrancar()}")
    print(f"• {moto.mostrar_tipo()}: {moto.arrancar()}")

    # === ENCAPSULACIÓN ===
    print("\n\n🔹 3. DEMOSTRACIÓN DE ENCAPSULACIÓN")
    print("-" * 40)

    cuenta = CuentaBancaria("Juan Tipantuna", "123456789", 1000)

    print(f"\n💳 Operaciones bancarias (datos protegidos):")
    print(cuenta.depositar(500))
    print(cuenta.retirar(200))

    print(f"\n📊 Saldo final: ${cuenta.get_saldo()}")
    print(f"🔒 Número cuenta (parcial): {cuenta.get_numero_cuenta()}")

    # === RESUMEN ===
    print("\n" + "=" * 70)
    print(" " * 15 + "✅ CONCEPTOS DEMOSTRADOS EXITOSAMENTE")
    print("=" * 70)

    conceptos = [
        "✓ HERENCIA: Automovil y Motocicleta heredan de Vehiculo",
        "✓ POLIMORFISMO: arrancar() tiene diferente implementación",
        "✓ ENCAPSULACIÓN: __saldo y __numero_cuenta son privados",
        "✓ ABSTRACCIÓN: Métodos ocultan complejidad interna",
        "✓ MODULARIDAD: Clases con responsabilidades únicas"
    ]

    for concepto in conceptos:
        print(concepto)

    print("\n" + "=" * 70)
    print(" " * 20 + "🎉 TAREA COMPLETADA")
    print("=" * 70)


# ======================
# EJECUCIÓN
# ======================
if __name__ == "__main__":
    main()