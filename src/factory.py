from persona import Conductor, Asistente


class Factory:
    def create_conductor(self) -> Conductor:
        pass

    def create_asistente(self) -> Asistente:
        pass


class TrashCityFactory(Factory):
    def create_conductor(self) -> Conductor:
        return Conductor(1, "Juan", "Perez", "123456", "A1234")

    def create_asistente(self) -> Asistente:
        return Asistente(2, "Maria", "Lopez", "789012", 1)
