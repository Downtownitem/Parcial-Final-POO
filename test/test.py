from datetime import date, time
import pytest

from main import (
    Asistente,
    Camion,
    CentroAcopio,
    Conductor,
    PuntoGeografico,
    Ruta,
    RutaEstrategiaA,
    SistemaInformacion,
    TrashCityFactory,
    Turno,
)


def test_punto_geografico():
    punto = PuntoGeografico(10.0, 20.0)
    assert punto.latitud == 10.0
    assert punto.longitud == 20.0


def test_persona():
    persona = Conductor(1, "Juan", "Perez", "123456", "A1234")
    assert persona.nombre == "Juan"
    assert persona.apellido == "Perez"


def test_camion_asignar_persona():
    conductor = Conductor(1, "Juan", "Perez", "123456", "A1234")
    asistente = Asistente(2, "Maria", "Lopez", "789012", 1)
    camion = Camion(1, "ABC123", 2010, {"vidrio": 0.0, "papel": 0.0}, True)
    camion.asignar_persona(conductor, "conductor")
    camion.asignar_persona(asistente, "asistente1")
    assert camion.conductor == conductor
    assert camion.asistente1 == asistente


def test_ruta():
    ruta_estrategia = RutaEstrategiaA()
    ruta = Ruta("TestRuta", ruta_estrategia)
    ruta.calcular_ruta()
    assert ruta.puntos == []


def test_turno():
    factory = TrashCityFactory()
    ruta_estrategia = RutaEstrategiaA()
    ruta = Ruta("TestRuta", ruta_estrategia)
    camion = Camion(1, "ABC123", 2010, {"vidrio": 0.0, "papel": 0.0}, True)
    turno = Turno(1, date.today(), time(8), time(17), camion, ruta, factory)
    assert turno.camion == camion
    assert turno.ruta == ruta


def test_sistema_informacion():
    sistema = SistemaInformacion()
    factory = TrashCityFactory()
    ruta_estrategia = RutaEstrategiaA()
    ruta = Ruta("TestRuta", ruta_estrategia)
    camion = Camion(1, "ABC123", 2010, {"vidrio": 1.0, "papel": 2.0}, True)
    turno = Turno(1, date.today(), time(8), time(17), camion, ruta, factory)
    sistema.turnos.append(turno)

    cantidad_vidrio = sistema.calcular_cantidad_de(date.today(), "vidrio")

    assert cantidad_vidrio == 0.0
