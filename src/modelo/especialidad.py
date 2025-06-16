from ..excepciones import DatosInvalidosException

class Especialidad:
    def __init__(self, tipo: str, dias: list[str]):
        if not tipo or not isinstance(tipo, str):
            raise DatosInvalidosException("El tipo de especialidad es requerido y debe ser texto")
        if not dias or not isinstance(dias, list) or len(dias) == 0:
            raise DatosInvalidosException("Debe especificar al menos un día de atención")
        
        dias_validos = ["lunes", "martes", "miercoles", "miércoles", "jueves", "viernes", "sabado", "sábado", "domingo"]
        dias_normalizados = []
        for dia in dias:
            dia_lower = dia.lower()
            if dia_lower not in dias_validos:
                raise DatosInvalidosException(f"Día inválido: {dia}")
            
            if dia_lower == "miercoles":
                dia_lower = "miércoles"
            elif dia_lower == "sabado":
                dia_lower = "sábado"
            dias_normalizados.append(dia_lower)
        
        self.__tipo = tipo
        self.__dias = dias_normalizados
    
    def obtener_especialidad(self) -> str:
        return self.__tipo
    
    def verificar_dia(self, dia: str) -> bool:

        dia_normalizado = dia.lower()
        if dia_normalizado == "miercoles":
            dia_normalizado = "miércoles"
        elif dia_normalizado == "sabado":
            dia_normalizado = "sábado"
        return dia_normalizado in self.__dias
    
    def obtener_dias(self) -> list[str]:
        return self.__dias.copy()
    
    def __str__(self) -> str:
        dias_str = ", ".join(self.__dias)
        return f"{self.__tipo} (Días: {dias_str})"