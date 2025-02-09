from pydantic import BaseModel
from typing import Optional

class CondominioBase(BaseModel):
    nome_do_condominio: str
    endereco: str
    num: str
    bairro: str
    cidade: str
    UF: str
    cep: str

class CondominioCreate(CondominioBase):
    pass

class CondominioUpdate(CondominioBase):
    pass

class Condominio(CondominioBase):
    uuid: str

    class Config:
        from_attributes = True 