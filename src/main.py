from sistema_de_informacion import SistemaInformacion
from factory import TrashCityFactory
from camion import Camion
from strategy import RutaEstrategiaA
from ruta import Ruta
from punto_geografico import PuntoGeografico
from centro_acopio import CentroAcopio
from turno import Turno
from datetime import date, time

sistema = SistemaInformacion()

factory = TrashCityFactory()
conductor = factory.create_conductor()
asistente = factory.create_asistente()

camion = Camion(1, "ABC123", 2010, {"vidrio": 0.0, "papel": 0.0}, True)
camion.asignar_persona(conductor, "conductor")
camion.asignar_persona(asistente, "asistente1")

ruta_estrategia = RutaEstrategiaA()
ruta = Ruta("TestRuta", ruta_estrategia)
ruta.calcular_ruta()

ubicacion_acopio = PuntoGeografico(10.0, 20.0)
acopio = CentroAcopio(1, ubicacion_acopio)

turno = Turno(1, date.today(), time(8), time(17), camion, ruta, factory)

sistema.turnos.append(turno)
sistema.centros_acopio.append(acopio)

while True:
    print("Seleccione una opción:")
    print("1: Calcular cantidad de un objeto en un día específico")
    print("2: Salir")
    opcion = int(input("Opción: "))

    if opcion == 1:
        dia_str = input("Ingrese la fecha en formato YYYY-MM-DD: ")
        dia = date.fromisoformat(dia_str)
        objeto = input("Ingrese el tipo de objeto: ")
        cantidad = sistema.calcular_cantidad_de(dia, objeto)
        print(f"La cantidad de {objeto} en {dia_str} es: {cantidad}")
    elif opcion == 2:
        break
    else:
        print("Opción no válida")
