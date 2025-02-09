from typing import List, Optional
from app.models.condominio import Condominio
from app.schemas.condominio import CondominioCreate, CondominioUpdate

class CondominioService:
    def __init__(self):
        self.condominios: List[Condominio] = []
        self._popular_dados_iniciais()

    def _popular_dados_iniciais(self):
        """Popula a lista com dados iniciais de condomínios"""
        dados_iniciais = [
            {
                "nome_do_condominio": "Residencial Vila Olímpia",
                "endereco": "Rua Frei Aureliano de Grotamare",
                "num": "251",
                "bairro": "SIM",
                "cidade": "Feira de Santana",
                "UF": "BA"
            },
            {
                "nome_do_condominio": "Condomínio Terra Nova Feira",
                "endereco": "Avenida Artêmia Pires Freitas",
                "num": "1510",
                "bairro": "SIM",
                "cidade": "Feira de Santana",
                "UF": "BA"
            },
            {
                "nome_do_condominio": "Condomínio Green Park",
                "endereco": "Rua Frei Aureliano de Grotamare",
                "num": "894",
                "bairro": "SIM",
                "cidade": "Feira de Santana",
                "UF": "BA"
            },
            {
                "nome_do_condominio": "Condomínio Reserva Feira",
                "endereco": "Avenida Artêmia Pires Freitas",
                "num": "741",
                "bairro": "SIM",
                "cidade": "Feira de Santana",
                "UF": "BA"
            },
            {
                "nome_do_condominio": "Residencial Le Parc",
                "endereco": "Rua Frei Aureliano de Grotamare",
                "num": "300",
                "bairro": "SIM",
                "cidade": "Feira de Santana",
                "UF": "BA"
            },
            {
                "nome_do_condominio": "Condomínio Parque Flora",
                "endereco": "Avenida Artêmia Pires Freitas",
                "num": "1200",
                "bairro": "SIM",
                "cidade": "Feira de Santana",
                "UF": "BA"
            },
            {
                "nome_do_condominio": "Residencial Viva Mais",
                "endereco": "Avenida Artêmia Pires Freitas",
                "num": "520",
                "bairro": "SIM",
                "cidade": "Feira de Santana",
                "UF": "BA"
            },
            {
                "nome_do_condominio": "Condomínio Alameda Flores",
                "endereco": "Rua São Vicente",
                "num": "455",
                "bairro": "SIM",
                "cidade": "Feira de Santana",
                "UF": "BA"
            },
            {
                "nome_do_condominio": "Condomínio Villa dos Pássaros",
                "endereco": "Rua Padre Antônio Vieira",
                "num": "632",
                "bairro": "SIM",
                "cidade": "Feira de Santana",
                "UF": "BA"
            },
            {
                "nome_do_condominio": "Residencial Vista do SIM",
                "endereco": "Avenida Artêmia Pires Freitas",
                "num": "900",
                "bairro": "SIM",
                "cidade": "Feira de Santana",
                "UF": "BA"
            },
            # Santa Mônica
            {
                "nome_do_condominio": "Residencial Parque das Acácias",
                "endereco": "Avenida Deputado Colbert Martins",
                "num": "250",
                "bairro": "Santa Mônica",
                "cidade": "Feira de Santana",
                "UF": "BA"
            },
            {
                "nome_do_condominio": "Condomínio Villa Jardins",
                "endereco": "Avenida Deputado Colbert Martins",
                "num": "1800",
                "bairro": "Santa Mônica",
                "cidade": "Feira de Santana",
                "UF": "BA"
            },
            # Tomba
            {
                "nome_do_condominio": "Condomínio Solar Princesa do Sertão",
                "endereco": "Avenida Eduardo Fróes da Mota",
                "num": "2500",
                "bairro": "Tomba",
                "cidade": "Feira de Santana",
                "UF": "BA"
            },
            # Cidade Nova
            {
                "nome_do_condominio": "Residencial Cidade Nova",
                "endereco": "Avenida João Durval Carneiro",
                "num": "3000",
                "bairro": "Cidade Nova",
                "cidade": "Feira de Santana",
                "UF": "BA"
            }
        ]

        for dados in dados_iniciais:
            condominio = Condominio(
                nome_do_condominio=dados["nome_do_condominio"],
                endereco=dados["endereco"],
                num=dados["num"],
                bairro=dados["bairro"],
                cidade=dados["cidade"],
                UF=dados["UF"]
            )
            self.condominios.append(condominio)

    def create(self, condominio: CondominioCreate) -> Condominio:
        db_condominio = Condominio(
            nome_do_condominio=condominio.nome_do_condominio,
            endereco=condominio.endereco,
            num=condominio.num,
            bairro=condominio.bairro,
            cidade=condominio.cidade,
            UF=condominio.UF
        )
        self.condominios.append(db_condominio)
        return db_condominio

    def get_all(
        self,
        nome: Optional[str] = None,
        cidade: Optional[str] = None,
        bairro: Optional[str] = None
    ) -> List[Condominio]:
        resultados = self.condominios

        if nome:
            resultados = [c for c in resultados if nome.lower() in c.nome_do_condominio.lower()]
        if cidade:
            resultados = [c for c in resultados if cidade.lower() in c.cidade.lower()]
        if bairro:
            resultados = [c for c in resultados if bairro.lower() in c.bairro.lower()]

        return resultados

    def get_by_uuid(self, uuid: str) -> Optional[Condominio]:
        for condominio in self.condominios:
            if condominio.uuid == uuid:
                return condominio
        return None

    def update(self, uuid: str, condominio_data: CondominioUpdate) -> Optional[Condominio]:
        condominio = self.get_by_uuid(uuid)
        if condominio:
            condominio.nome_do_condominio = condominio_data.nome_do_condominio
            condominio.endereco = condominio_data.endereco
            condominio.num = condominio_data.num
            condominio.bairro = condominio_data.bairro
            condominio.cidade = condominio_data.cidade
            condominio.UF = condominio_data.UF
            return condominio
        return None

    def delete(self, uuid: str) -> bool:
        for i, condominio in enumerate(self.condominios):
            if condominio.uuid == uuid:
                del self.condominios[i]
                return True
        return False

    def get_statistics(self):
        contagem_por_bairro = {}
        for condominio in self.condominios:
            if condominio.bairro in contagem_por_bairro:
                contagem_por_bairro[condominio.bairro] += 1
            else:
                contagem_por_bairro[condominio.bairro] = 1
        
        return {
            "total_condominios": len(self.condominios),
            "condominios_por_bairro": contagem_por_bairro
        } 