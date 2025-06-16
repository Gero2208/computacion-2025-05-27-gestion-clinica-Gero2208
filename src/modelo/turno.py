from datetime import datetime
from ..excepciones import DatosInvalidosException, MedicoNoDisponibleException, EspecialidadInvalidaException
from .paciente import Paciente
from .medico import Medico

class Turno:

    def __init__(self, paciente: Paciente, medico: Medico, fecha: str, hora: str, especialidad: str):

        if not isinstance(paciente, Paciente):
            raise DatosInvalidosException("Se requiere un objeto Paciente válido")
        if not isinstance(medico, Medico):
            raise DatosInvalidosException("Se requiere un objeto Médico válido")
        if not fecha or not isinstance(fecha, str):
            raise DatosInvalidosException("La fecha es requerida y debe ser texto")
        if not hora or not isinstance(hora, str):
            raise DatosInvalidosException("La hora es requerida y debe ser texto")
        if not especialidad or not isinstance(especialidad, str):
            raise DatosInvalidosException("La especialidad es requerida y debe ser texto")
        
        try:
            fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
            dia_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"][fecha_obj.weekday()]
            
            esp_disponible = medico.obtener_especialidad_para_dia(dia_semana)
            if not esp_disponible:
                raise MedicoNoDisponibleException(f"El médico no atiende los {dia_semana}")
            if esp_disponible != especialidad:
                raise EspecialidadInvalidaException(f"El médico atiende {esp_disponible} los {dia_semana}, no {especialidad}")
        except ValueError:
            raise DatosInvalidosException(f"Formato de fecha inválido: {fecha}. Use dd/mm/aaaa")
        
        try:
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            raise DatosInvalidosException(f"Formato de hora inválido: {hora}. Use HH:MM")
        
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha = fecha
        self.__hora = hora
        self.__especialidad = especialidad
        self.__estado = "Programado" 
    
    def obtener_paciente(self) -> Paciente:
        return self.__paciente
    
    def obtener_medico(self) -> Medico:
        return self.__medico
    
    def obtener_fecha(self) -> str:
        return self.__fecha
    
    def obtener_hora(self) -> str:
        return self.__hora
    
    def obtener_especialidad(self) -> str:
        return self.__especialidad
    
    def marcar_completado(self):
        self.__estado = "Completado"
    
    def marcar_cancelado(self):
        self.__estado = "Cancelado"
    
    def obtener_estado(self) -> str:
        return self.__estado
    
    def __str__(self) -> str:
        return f"Turno: {self.__fecha} {self.__hora} - Paciente: {self.__paciente.obtener_nombre()} (DNI: {self.__paciente.obtener_dni()}) - " \
               f"Dr/a. {self.__medico.obtener_nombre()} - {self.__especialidad} - Estado: {self.__estado}"