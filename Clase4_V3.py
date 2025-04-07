# -------------------- CLASE MASCOTA HOSPITALIZADA --------------------
class MascotaHospitalizada:
    def __init__(self, historia_clinica, nombre, tipo, peso, fecha_ingreso, medicamento):
        self.historia_clinica = historia_clinica
        self.nombre = nombre
        self.tipo = tipo
        self.peso = peso
        self.fecha_ingreso = fecha_ingreso
        self.medicamento = medicamento

    # Getters
    def get_historia_clinica(self):
        return self.historia_clinica

    def get_nombre(self):
        return self.nombre

    def get_tipo(self):
        return self.tipo

    def get_peso(self):
        return self.peso

    def get_fecha_ingreso(self):
        return self.fecha_ingreso

    def get_medicamento(self):
        return self.medicamento

    # Setters
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def set_tipo(self, nuevo_tipo):
        self.tipo = nuevo_tipo

    def set_peso(self, nuevo_peso):
        self.peso = nuevo_peso

    def set_fecha_ingreso(self, nueva_fecha):
        self.fecha_ingreso = nueva_fecha

    def set_medicamento(self, nuevo_medicamento):
        self.medicamento = nuevo_medicamento

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Historia: {self.historia_clinica}, Peso: {self.peso}kg, Ingreso: {self.fecha_ingreso}, Medicamento: {self.medicamento}"


# -------------------- LÓGICA DEL SISTEMA --------------------
hospital = []

def ingresar_mascota():
    if len(hospital) >= 10:
        print("🚫 No se pueden hospitalizar más mascotas. Límite alcanzado (10).")
        return

    historia = input("Número de historia clínica: ")
    for m in hospital:
        if m.get_historia_clinica() == historia:
            print("⚠️ Ya existe una mascota con ese número de historia clínica.")
            return

    nombre = input("Nombre: ")
    tipo = input("Tipo (canino/felino): ")
    peso = float(input("Peso (kg): "))
    fecha = input("Fecha de ingreso (dd/mm/aaaa): ")
    medicamento = input("Medicamento: ")

    mascota = MascotaHospitalizada(historia, nombre, tipo, peso, fecha, medicamento)
    hospital.append(mascota)
    print(f"✅ Mascota '{nombre}' hospitalizada.")

def ver_fecha_ingreso():
    historia = input("Ingrese número de historia clínica: ")
    for m in hospital:
        if m.get_historia_clinica() == historia:
            print(f"📅 Fecha de ingreso: {m.get_fecha_ingreso()}")
            return
    print("❌ Mascota no encontrada.")

def contar_mascotas():
    print(f"👥 Número de mascotas hospitalizadas: {len(hospital)}")

def ver_medicamento():
    historia = input("Ingrese número de historia clínica: ")
    for m in hospital:
        if m.get_historia_clinica() == historia:
            print(f"💊 Medicamento: {m.get_medicamento()}")
            return
    print("❌ Mascota no encontrada.")

def eliminar_mascota():
    historia = input("Ingrese número de historia clínica a eliminar: ")
    for m in hospital:
        if m.get_historia_clinica() == historia:
            hospital.remove(m)
            print("🗑️ Mascota eliminada del servicio.")
            return
    print("❌ Mascota no encontrada.")

# -------------------- MENÚ PRINCIPAL --------------------
def mostrar_menu():
    print("\n--- Menú Hospitalización Veterinaria ---")
    print("1. Ingresar mascota")
    print("2. Ver fecha de ingreso")
    print("3. Ver número de mascotas")
    print("4. Ver medicamento")
    print("5. Eliminar mascota")
    print("6. Salir")

def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_mascota()
        elif opcion == "2":
            ver_fecha_ingreso()
        elif opcion == "3":
            contar_mascotas()
        elif opcion == "4":
            ver_medicamento()
        elif opcion == "5":
            eliminar_mascota()
        elif opcion == "6":
            print("👋 Saliendo del sistema.")
            break
        else:
            print("❌ Opción inválida.")

# -------------------- INICIO DEL PROGRAMA --------------------
if __name__ == "__main__":
    ejecutar()
