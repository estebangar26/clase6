from datetime import datetime

class Mascota:
    def __init__(self, nombre, historia_clinica, tipo, peso, fecha_ingreso, medicamento):
        self.nombre = nombre
        self.historia_clinica = historia_clinica
        self.tipo = tipo
        self.peso = peso
        self.fecha_ingreso = fecha_ingreso  # objeto datetime.date
        self.medicamento = medicamento

    def __str__(self):
        return (f"[{self.historia_clinica}] {self.nombre} ({self.tipo}) - Peso: {self.peso}kg - "
                f"Ingreso: {self.fecha_ingreso.strftime('%d/%m/%Y')} - Medicamento: {self.medicamento}")

    def get_fecha_ingreso(self):
        return self.fecha_ingreso

    def get_medicamento(self):
        return self.medicamento

    def eliminar_medicamento(self):
        self.medicamento = None

class HospitalVeterinario:
    def __init__(self):
        self.caninos = {}
        self.felinos = {}
        self.medicamentos = set()

    def agregar_mascota(self, mascota):
        if len(self.caninos) + len(self.felinos) >= 10:
            print("❌ El hospital ya está lleno. Máximo 10 pacientes.")
            return

        if mascota.historia_clinica in self.caninos or mascota.historia_clinica in self.felinos:
            print("❌ Ya existe una mascota con ese número de historia clínica.")
            return

        if mascota.medicamento in self.medicamentos:
            print("❌ Ya hay una mascota con ese medicamento. No se permiten duplicados.")
            return

        if mascota.tipo.lower() == "canino":
            self.caninos[mascota.historia_clinica] = mascota
        elif mascota.tipo.lower() == "felino":
            self.felinos[mascota.historia_clinica] = mascota
        else:
            print("❌ Tipo de mascota no válido.")
            return

        self.medicamentos.add(mascota.medicamento)
        print("✅ Mascota ingresada exitosamente.")

    def buscar_mascota(self, historia_clinica):
        return self.caninos.get(historia_clinica) or self.felinos.get(historia_clinica)

    def eliminar_mascota(self, historia_clinica):
        if historia_clinica in self.caninos:
            self.medicamentos.discard(self.caninos[historia_clinica].medicamento)
            del self.caninos[historia_clinica]
            print("🗑️ Canino eliminado.")
        elif historia_clinica in self.felinos:
            self.medicamentos.discard(self.felinos[historia_clinica].medicamento)
            del self.felinos[historia_clinica]
            print("🗑️ Felino eliminado.")
        else:
            print("❌ Mascota no encontrada.")

    def eliminar_medicamento_de_mascota(self, historia_clinica):
        mascota = self.buscar_mascota(historia_clinica)
        if mascota:
            self.medicamentos.discard(mascota.get_medicamento())
            mascota.eliminar_medicamento()
            print("💊 Medicamento eliminado de la mascota.")
        else:
            print("❌ Mascota no encontrada.")

    def mostrar_fecha_ingreso(self, historia_clinica):
        mascota = self.buscar_mascota(historia_clinica)
        if mascota:
            print(f"📅 Fecha de ingreso: {mascota.get_fecha_ingreso().strftime('%d/%m/%Y')}")
        else:
            print("❌ Mascota no encontrada.")

    def contar_pacientes(self):
        total = len(self.caninos) + len(self.felinos)
        print(f"👥 Total de mascotas hospitalizadas: {total}")

    def mostrar_medicamento(self, historia_clinica):
        mascota = self.buscar_mascota(historia_clinica)
        if mascota:
            if mascota.get_medicamento():
                print(f"💊 Medicamento: {mascota.get_medicamento()}")
            else:
                print("⚠️ La mascota no tiene medicamento asignado.")
        else:
            print("❌ Mascota no encontrada.")

def ingresar_fecha():
    fecha_str = input("Fecha de ingreso (dd/mm/aaaa): ")
    try:
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y").date()
        return fecha
    except ValueError:
        print("❌ Formato de fecha inválido. Use dd/mm/aaaa.")
        return None

def menu():
    hospital = HospitalVeterinario()
    while True:
        print("\n--- MENÚ HOSPITAL VETERINARIO ---")
        print("1. Ingresar mascota")
        print("2. Ver fecha de ingreso")
        print("3. Ver número de mascotas")
        print("4. Ver medicamento")
        print("5. Eliminar mascota")
        print("6. Eliminar medicamento de mascota")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            historia = input("Historia clínica: ")
            tipo = input("Tipo (canino/felino): ").lower()
            peso = float(input("Peso: "))
            fecha = ingresar_fecha()
            if not fecha:
                continue
            medicamento = input("Medicamento: ")
            mascota = Mascota(nombre, historia, tipo, peso, fecha, medicamento)
            hospital.agregar_mascota(mascota)

        elif opcion == "2":
            historia = input("Historia clínica: ")
            hospital.mostrar_fecha_ingreso(historia)

        elif opcion == "3":
            hospital.contar_pacientes()

        elif opcion == "4":
            historia = input("Historia clínica: ")
            hospital.mostrar_medicamento(historia)

        elif opcion == "5":
            historia = input("Historia clínica a eliminar: ")
            hospital.eliminar_mascota(historia)

        elif opcion == "6":
            historia = input("Historia clínica: ")
            hospital.eliminar_medicamento_de_mascota(historia)

        elif opcion == "7":
            print("👋 Hasta luego.")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    menu()
