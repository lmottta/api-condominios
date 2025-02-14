from typing import List, Optional
from app.models.condominio import Condominio
from app.schemas.condominio import CondominioCreate, CondominioUpdate
import random

class CondominioService:
    def __init__(self):
        self.condominios: List[Condominio] = []
        self._popular_dados_iniciais()

    def _popular_dados_iniciais(self):
        """Popula a lista com dados iniciais de condomínios"""
        # Dados base para geração de condomínios
        bairros_feira = [
            "SIM", "Santa Mônica", "Tomba", "Mangabeira", "Papagaio", "Caseb",
            "Cidade Nova", "Conceição", "Feira IX", "Feira X", "Muchila",
            "Parque Ipê", "Ponto Central", "Queimadinha", "Santo Antônio dos Prazeres",
            "Capuchinhos", "Sobradinho", "Brasília", "Jardim Cruzeiro", "Serraria Brasil",
            "Jardim Acácia", "Asa Branca", "Pedra do Descanso", "Parque Getúlio Vargas",
            "Campo do Gado", "Campo Limpo", "Centro", "Gabriela", "Kalilândia", "Novo Horizonte"
        ]
        
        avenidas_principais = [
            "Avenida Artêmia Pires", "Avenida Fraga Maia", "Avenida João Durval",
            "Avenida Getúlio Vargas", "Avenida Maria Quitéria", "Avenida Nóide Cerqueira",
            "Avenida José Falcão", "Avenida Presidente Dutra", "Avenida Eduardo Fróes da Mota",
            "Avenida Senhor dos Passos"
        ]
        
        ruas = [
            "Rua Professora Edelvira de Oliveira", "Rua Frei Felix de Pacaembu",
            "Rua Voluntários da Pátria", "Rua Japão", "Rua São Domingos",
            "Rua Castro Alves", "Rua Boticário Moncorvo", "Rua Comandante Almiro",
            "Rua Cristóvão Colombo", "Rua da Aurora", "Rua Domingos Barbosa",
            "Rua Floriano Peixoto", "Rua Geminiano Costa", "Rua Intendente Abdon",
            "Rua Juvêncio Erudilho", "Rua Leonídio Rocha", "Rua Marechal Deodoro",
            "Rua Nova", "Rua Olímpio Vital", "Rua Pedro Suzart"
        ]
        
        prefixos = [
            "Residencial", "Condomínio", "Edifício", "Park", "Village", "Plaza",
            "Garden", "Parque", "Solar", "Palace", "Mansão", "Morada", "Jardins",
            "Reserva", "Bosque", "Ville", "Premium", "Eco", "Life", "Club"
        ]
        
        nomes = [
            "Primavera", "Horizonte", "Vista Bela", "Jardim", "Sol Nascente",
            "Bela Vista", "Monte Verde", "Serra Dourada", "Vale Verde", "Recanto",
            "das Flores", "dos Pássaros", "Imperial", "Real", "Elite", "Premium",
            "Privilege", "Classic", "Elegance", "Excellence", "Supreme", "Noble",
            "Golden", "Diamond", "Platinum", "Crystal", "Royal", "Imperial",
            "Paradise", "Oasis", "Splendor", "Harmony", "Serenity", "Victory",
            "Legacy", "Heritage", "Prestige", "Essence", "Unique", "Prime"
        ]
        
        complementos = [
            "I", "II", "III", "IV", "V", "Premium", "Plus", "Elite", "Classic",
            "Master", "VIP", "Special", "Exclusive", "Superior", "Prime"
        ]

        # Adicionar condomínios existentes primeiro
        condominios_existentes = [
            # Condomínios do SIM com endereços reais verificados
            {
                "nome": "Residencial Vila Olímpia",
                "endereco": "Rua Frei Aureliano de Grotamare",
                "bairro": "SIM",
                "num": "251",
                "cep": "44085-132"
            },
            {
                "nome": "Condomínio Terra Nova Feira",
                "endereco": "Avenida Artêmia Pires Freitas",
                "bairro": "SIM",
                "num": "1510",
                "cep": "44085-370"
            },
            {
                "nome": "Condomínio Green Park",
                "endereco": "Rua Frei Aureliano de Grotamare",
                "bairro": "SIM",
                "num": "894",
                "cep": "44085-132"
            },
            {
                "nome": "Condomínio Reserva Feira",
                "endereco": "Avenida Artêmia Pires Freitas",
                "bairro": "SIM",
                "num": "741",
                "cep": "44085-370"
            },
            {
                "nome": "Residencial Le Parc",
                "endereco": "Rua Frei Aureliano de Grotamare",
                "bairro": "SIM",
                "num": "300",
                "cep": "44085-132"
            },
            {
                "nome": "Condomínio Parque Flora",
                "endereco": "Avenida Artêmia Pires Freitas",
                "bairro": "SIM",
                "num": "8147",
                "cep": "44085-370"
            },
            {
                "nome": "Residencial Viva Mais",
                "endereco": "Avenida Artêmia Pires Freitas",
                "bairro": "SIM",
                "num": "520",
                "cep": "44085-370"
            },
            {
                "nome": "Condomínio Alameda Flores",
                "endereco": "Rua São Vicente",
                "bairro": "SIM",
                "num": "455",
                "cep": "44085-060"
            },
            {
                "nome": "Condomínio Villa dos Pássaros",
                "endereco": "Rua Padre Antônio Vieira",
                "bairro": "SIM",
                "num": "632",
                "cep": "44085-100"
            },
            {
                "nome": "Residencial Vista do SIM",
                "endereco": "Avenida Artêmia Pires Freitas",
                "bairro": "SIM",
                "num": "900",
                "cep": "44085-370"
            },
            # Novos condomínios do SIM
            {
                "nome": "Condomínio Bella Vista",
                "endereco": "Rua Frei Aureliano de Grotamare",
                "bairro": "SIM",
                "num": "500",
                "cep": "44085-132"
            },
            {
                "nome": "Residencial Jardim Acácia",
                "endereco": "Avenida Artêmia Pires Freitas",
                "bairro": "SIM",
                "num": "1100",
                "cep": "44085-370"
            },
            # Santa Mônica
            {
                "nome": "Residencial Parque das Acácias",
                "endereco": "Avenida Deputado Colbert Martins",
                "bairro": "Santa Mônica",
                "num": "250",
                "cep": "44077-060"
            },
            {
                "nome": "Condomínio Villa Jardins",
                "endereco": "Avenida Deputado Colbert Martins",
                "bairro": "Santa Mônica",
                "num": "1800",
                "cep": "44077-060"
            },
            {
                "nome": "Residencial Santa Mônica",
                "endereco": "Avenida Deputado Colbert Martins",
                "bairro": "Santa Mônica",
                "num": "1500",
                "cep": "44077-060"
            },
            # Tomba
            {
                "nome": "Condomínio Solar Princesa do Sertão",
                "endereco": "Avenida Eduardo Fróes da Mota",
                "bairro": "Tomba",
                "num": "2500",
                "cep": "44091-000"
            },
            {
                "nome": "Residencial Tomba",
                "endereco": "Avenida Eduardo Fróes da Mota",
                "bairro": "Tomba",
                "num": "3000",
                "cep": "44091-000"
            },
            # Cidade Nova
            {
                "nome": "Residencial Cidade Nova",
                "endereco": "Avenida João Durval Carneiro",
                "bairro": "Cidade Nova",
                "num": "3000",
                "cep": "44053-715"
            },
            {
                "nome": "Condomínio Portal da Cidade",
                "endereco": "Avenida João Durval Carneiro",
                "bairro": "Cidade Nova",
                "num": "2500",
                "cep": "44053-715"
            },
            # Muchila
            {
                "nome": "Residencial Muchila",
                "endereco": "Rua Professora Germiniana da Silva Alves",
                "bairro": "Muchila",
                "num": "600",
                "cep": "44024-054"
            }
        ]

        # Adicionar os condomínios existentes
        for cond in condominios_existentes:
            condominio = Condominio(
                nome_do_condominio=cond["nome"],
                endereco=cond["endereco"],
                num=cond["num"],
                bairro=cond["bairro"],
                cidade="Feira de Santana",
                UF="BA",
                cep=cond["cep"]
            )
            self.condominios.append(condominio)

        # Gerar novos condomínios até completar 1000
        enderecos_usados = set()
        while len(self.condominios) < 1000:
            # Gerar endereço único
            rua = random.choice(avenidas_principais + ruas)
            num = str(random.randint(1, 50) * 100)
            endereco_completo = f"{rua}_{num}"
            
            if endereco_completo not in enderecos_usados:
                enderecos_usados.add(endereco_completo)
                
                # Gerar nome único do condomínio
                prefixo = random.choice(prefixos)
                nome = random.choice(nomes)
                complemento = random.choice(complementos) if random.random() > 0.5 else ""
                nome_completo = f"{prefixo} {nome} {complemento}".strip()
                
                # Definir CEP baseado no bairro
                bairro = random.choice(bairros_feira)
                cep = "44000-000"  # CEP base para Feira de Santana
                
                condominio = Condominio(
                    nome_do_condominio=nome_completo,
                    endereco=rua,
                    num=num,
                    bairro=bairro,
                    cidade="Feira de Santana",
                    UF="BA",
                    cep=cep
                )
                self.condominios.append(condominio)

    def create(self, condominio: CondominioCreate) -> Condominio:
        db_condominio = Condominio(
            nome_do_condominio=condominio.nome_do_condominio,
            endereco=condominio.endereco,
            num=condominio.num,
            bairro=condominio.bairro,
            cidade=condominio.cidade,
            UF=condominio.UF,
            cep=condominio.cep
        )
        self.condominios.append(db_condominio)
        return db_condominio

    def get_all(
        self,
        nome: Optional[str] = None,
        cidade: Optional[str] = None,
        bairro: Optional[str] = None,
        skip: int = 0,
        limit: int = 100
    ) -> dict:
        resultados = self.condominios

        if nome:
            resultados = [c for c in resultados if nome.lower() in c.nome_do_condominio.lower()]
        if cidade:
            resultados = [c for c in resultados if cidade.lower() in c.cidade.lower()]
        if bairro:
            resultados = [c for c in resultados if bairro.lower() in c.bairro.lower()]

        total = len(resultados)
        total_paginas = (total + limit - 1) // limit
        pagina_atual = (skip // limit) + 1

        return {
            "total": total,
            "pagina_atual": pagina_atual,
            "total_paginas": total_paginas,
            "items": resultados[skip:skip + limit]
        }

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