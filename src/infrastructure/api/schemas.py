from pydantic import BaseModel, Field
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    token: str
    token_type: str

class Transaccion(BaseModel):
    segundos_desde_inicio: float = Field(..., alias="Time")
    variacion_comportamiento_1: float = Field(..., alias="V1")
    variacion_comportamiento_2: float = Field(..., alias="V2")
    variacion_comportamiento_3: float = Field(..., alias="V3")
    variacion_comportamiento_4: float = Field(..., alias="V4")
    variacion_comportamiento_5: float = Field(..., alias="V5")
    variacion_comportamiento_6: float = Field(..., alias="V6")
    variacion_comportamiento_7: float = Field(..., alias="V7")
    variacion_comportamiento_8: float = Field(..., alias="V8")
    variacion_comportamiento_9: float = Field(..., alias="V9")
    variacion_comportamiento_10: float = Field(..., alias="V10")
    variacion_comportamiento_11: float = Field(..., alias="V11")
    variacion_comportamiento_12: float = Field(..., alias="V12")
    variacion_comportamiento_13: float = Field(..., alias="V13")
    variacion_comportamiento_14: float = Field(..., alias="V14")
    variacion_comportamiento_15: float = Field(..., alias="V15")
    variacion_comportamiento_16: float = Field(..., alias="V16")
    variacion_comportamiento_17: float = Field(..., alias="V17")
    variacion_comportamiento_18: float = Field(..., alias="V18")
    variacion_comportamiento_19: float = Field(..., alias="V19")
    variacion_comportamiento_20: float = Field(..., alias="V20")
    variacion_comportamiento_21: float = Field(..., alias="V21")
    variacion_comportamiento_22: float = Field(..., alias="V22")
    variacion_comportamiento_23: float = Field(..., alias="V23")
    variacion_comportamiento_24: float = Field(..., alias="V24")
    variacion_comportamiento_25: float = Field(..., alias="V25")
    variacion_comportamiento_26: float = Field(..., alias="V26")
    variacion_comportamiento_27: float = Field(..., alias="V27")
    variacion_comportamiento_28: float = Field(..., alias="V28")
    monto_transaccion: float = Field(..., alias="Amount")

    class Config:
        populate_by_name = True

