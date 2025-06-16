from ..excepciones import DatosInvalidosException
from .especialidad import Especialidad

class Medico:

    def __init__(self, nombre: str, matricula: str):

        if not nombre or not isinstance(nombre, str):
            raise DatosInvalidosException("El nombre es requerido y debe ser texto")
        if not matricula or not isinstance(matricula, str):
            raise DatosInvalidosException("La matrícula es requerida y debe ser texto")
        
        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = []
    
    def agregar_especialidad(self, especialidad: Especialidad):

        if not isinstance(especialidad, Especialidad):
            raise DatosInvalidosException("Debe proporcionar un objeto de tipo Especialidad")
        
        for esp in self.__especialidades:
            if esp.obtener_especialidad() == especialidad.obtener_especialidad():
                raise DatosInvalidosException(f"El médico ya tiene la especialidad {especialidad.obtener_especialidad()}")
        
        self.__especialidades.append(especialidad)
    
    def obtener_matricula(self) -> str:
        return self.__matricula
    
    def obtener_nombre(self) -> str:
        return self.__nombre
    
    def obtener_especialidad_para_dia(self, dia: str) -> str | None:
        for especialidad in self.__especialidades:
            if especialidad.verificar_dia(dia):
                return especialidad.obtener_especialidad()
        return None
    
    def obtener_especialidades(self) -> list[Especialidad]:
        return self.__especialidades.copy()
    
    def __str__(self) -> str:
        if not self.__especialidades:
            return f"Dr/a. {self.__nombre} (Matrícula: {self.__matricula}) - Sin especialidades asignadas"
        
        especialidades_str = ", ".join([esp.obtener_especialidad() for esp in self.__especialidades])
        return f"Dr/a. {self.__nombre} (Matrícula: {self.__matricula}) - Especialidades: {especialidades_str}"