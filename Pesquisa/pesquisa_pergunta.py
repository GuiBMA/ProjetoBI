from datetime import datetime

class PesquisaPergunta:

    id_counter = 1
    def __init__(self):
        self.id = PesquisaPergunta.id_counter
        PesquisaPergunta.id_counter += 1

        self.pesquisa_id = None
        self.pesquisa_pergunta_tipo_id = None
        self.data_cadastro = None  # Tipo datetime
        self.ativo = True


    def set_pesquisa_id(self, pesquisa_id):
        self.pesquisa_id = pesquisa_id
        return self

    def set_pesquisa_pergunta_tipo_id(self, pesquisa_pergunta_tipo_id):
        self.pesquisa_pergunta_tipo_id = pesquisa_pergunta_tipo_id
        return self

    def set_data_cadastro(self, data_cadastro: datetime = None):
        self.data_cadastro = data_cadastro or datetime.now()
        return self

    def set_ativo(self, ativo):
        self.ativo = ativo
        return self

    def to_dict(self):
        return {
            "id": self.id,
            "pesquisa_id": self.pesquisa_id,
            "pesquisa_pergunta_tipo_id": self.pesquisa_pergunta_tipo_id,
            "data_cadastro": self.data_cadastro.isoformat() if self.data_cadastro else None,
            "ativo": self.ativo
        }

    def build(self):
        return self
