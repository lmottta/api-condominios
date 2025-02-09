from typing import Optional
import uuid as uuid_pkg

class Condominio:
    def __init__(
        self,
        nome_do_condominio: str,
        endereco: str,
        num: str,
        bairro: str,
        cidade: str,
        UF: str,
        cep: str,
        uuid: Optional[str] = None
    ):
        self.uuid = uuid if uuid else str(uuid_pkg.uuid4())
        self.nome_do_condominio = nome_do_condominio
        self.endereco = endereco
        self.num = num
        self.bairro = bairro
        self.cidade = cidade
        self.UF = UF
        self.cep = cep 