from enum import Enum

class TipoIntegracion:
    INTEGRA_DATOS = "Point-toPoint"
    INTEGRA_API = "Comunicación entra APIs"
    INTEGRA_LEGACY = "Conecta con cloud, arquitectura middleware"
    INTEGRA_iPaaS = "Plataformas centralizadas con conectores visuales"

class EstadoIntegracion(Enum):
    PENDIENTE = "pendiente"
    EN_RUTA = "en_ruta"
    ENTREGADO = "entregado"
    CANCELADO = "cancelado"
    EXCEPCION = "excepcion"

class Prioridad(Enum):
    BAJA = "baja"
    NORMAL = "normal"
    ALTA = "alta"
    URGENTE = "urgente"