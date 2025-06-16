from ..excepciones import DatosInvalidosException
from .paciente import Paciente
from .turno import Turno
from .receta import Receta

class HistoriaClinica:

    def __init__(self, paciente: Paciente):

        if not isinstance(paciente, Paciente):
            raise DatosInvalidosException("Se requiere un objeto Paciente válido")
        
        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []
    
    def agregar_turno(self, turno: Turno):

        if not isinstance(turno, Turno):
            raise DatosInvalidosException("Se requiere un objeto Turno válido")
        
        if turno.obtener_paciente().obtener_dni() != self.__paciente.obtener_dni():
            raise DatosInvalidosException("El turno no corresponde a este paciente")
        
        self.__turnos.append(turno)
    
    def agregar_receta(self, receta: Receta):

        if not isinstance(receta, Receta):
            raise DatosInvalidosException("Se requiere un objeto Receta válido")
        
        if receta.obtener_paciente().obtener_dni() != self.__paciente.obtener_dni():
            raise DatosInvalidosException("La receta no corresponde a este paciente")
        
        self.__recetas.append(receta)
    
    def obtener_paciente(self) -> Paciente:
        return self.__paciente
    
    def obtener_turnos(self) -> list[Turno]:
        return self.__turnos.copy()
    
    def obtener_recetas(self) -> list[Receta]:
        return self.__recetas.copy()
    
    def __str__(self) -> str:
        return f"Historia Clínica de {self.__paciente.obtener_nombre()} (DNI: {self.__paciente.obtener_dni()}) - " \
               f"{len(self.__turnos)} turnos, {len(self.__recetas)} recetas"