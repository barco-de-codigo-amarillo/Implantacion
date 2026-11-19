from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.enum.integra_enum import TipoIntegracion, EstadoIntegracion, Prioridad

class ArquitecturaCreate(BaseModel):
    id: int
    tipo: TipoIntegracion
    origen: str = Field(..., min_length=1, description="Integrado según criterio desde origen con código o dirección")
    destino: str = Field(..., min_length=1, description="Dirección o código de destino")
    agente: Optional[str] = Field(None, description="Agente de integración")
    notas: Optional[str] = None

class ArquitecturaResponse(BaseModel):
    id: int
    num_guia: str
    tipo: TipoIntegracion
    estado: EstadoIntegracion
    origen: str
    destino: str
    agente: Optional[str]
    empleado: Optional[str]
    prioridad: Prioridad
    notas: Optional[str]
    fecha_creacion: datetime
    fecha_entrega: Optional[datetime]


class Config: 
    from_attributes = True

