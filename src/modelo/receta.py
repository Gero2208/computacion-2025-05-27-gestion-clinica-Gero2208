from datetime import datetime
from ..excepciones import DatosInvalidosException
from .paciente import Paciente
from .medico import Medico

class Receta:

    def __init__(self, paciente: Paciente, medico: Medico, fecha: str, medicamentos: list[str], indicaciones: str):

        if not isinstance(paciente, Paciente):
            raise DatosInvalidosException("Se requiere un objeto Paciente válido")
        if not isinstance(medico, Medico):
            raise DatosInvalidosException("Se requiere un objeto Médico válido")
        if not fecha or not isinstance(fecha, str):
            raise DatosInvalidosException("La fecha es requerida y debe ser texto")
        if not isinstance(medicamentos, list) or not medicamentos:
            raise DatosInvalidosException("Debe proporcionar al menos un medicamento")
        if not indicaciones or not isinstance(indicaciones, str):
            raise DatosInvalidosException("Las indicaciones son requeridas y deben ser texto")
        
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            raise DatosInvalidosException(f"Formato de fecha inválido: {fecha}. Use dd/mm/aaaa")
        
        for medicamento in medicamentos:
            if not medicamento or not isinstance(medicamento, str):
                raise DatosInvalidosException("Todos los medicamentos deben ser texto válido")
        
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha = fecha
        self.__medicamentos = medicamentos
        self.__indicaciones = indicaciones
    
    def obtener_paciente(self) -> Paciente:
        return self.__paciente
    
    def obtener_medico(self) -> Medico:
        return self.__medico
    
    def obtener_fecha(self) -> str:
        return self.__fecha
    
    def obtener_medicamentos(self) -> list[str]:
        return self.__medicamentos.copy()
    
    def obtener_indicaciones(self) -> str:
        return self.__indicaciones
    
    def __str__(self) -> str:
        medicamentos_str = ", ".join(self.__medicamentos)
        return f"Receta ({self.__fecha}) - Paciente: {self.__paciente.obtener_nombre()} (DNI: {self.__paciente.obtener_dni()}) - " \
               f"Dr/a. {self.__medico.obtener_nombre()} - Medicamentos: {medicamentos_str}"