from datetime import date, datetime

class Pesquisa:

    id_counter = 1
    def __init__(self):
        self.id = Pesquisa.id_counter
        Pesquisa.id_counter += 1

        self.pesquisa_nome = None
        self.data_inicio = None
        self.data_fim = None
        self.data_cadastro = None
        self.ativo = True
        self.pesquisa_id = pesquisa_id
        return self

    def set_pesquisa_nome(self, pesquisa_nome):
        self.pesquisa_nome = pesquisa_nome
        return self

    def set_data_inicio(self, data_inicio: date):
        self.data_inicio = data_inicio
        return self

    def set_data_fim(self, data_fim: date):
        self.data_fim = data_fim
        return self

    def set_data_cadastro(self, data_cadastro: datetime = None):
        self.data_cadastro = data_cadastro or datetime.now()
        return self

    def set_ativo(self, ativo):
        self.ativo = ativo
        return self

    def to_dict(self):
        return {
            "pesquisa_id": self.id,
            "pesquisa_nome": self.pesquisa_nome,
            "data_inicio": self.data_inicio.isoformat() if self.data_inicio else None,
            "data_fim": self.data_fim.isoformat() if self.data_fim else None,
            "data_cadastro": self.data_cadastro.isoformat() if self.data_cadastro else None,
            "ativo": self.ativo
        }

    def build(self):
        return self
