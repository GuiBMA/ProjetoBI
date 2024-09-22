from datetime import datetime

class PesquisaPerguntaOpcao:

    id_counter = 1 
    def __init__(self):
        self.id = PesquisaPerguntaOpcao.id_counter
        PesquisaPerguntaOpcao.id_counter += 1

        self.pesquisa_pergunta_id = None
        self.indice = 1
        self.opcao = None
        self.data_cadastro = None  # Tipo datetime
        self.ativo = True


    def set_pesquisa_pergunta_id(self, pesquisa_pergunta_id):
        self.pesquisa_pergunta_id = pesquisa_pergunta_id
        return self

    def set_indice(self, indice):
        self.indice = indice
        return self

    def set_opcao(self, opcao):
        self.opcao = opcao
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
            "pesquisa_pergunta_id": self.pesquisa_pergunta_id,
            "indice": self.indice,
            "opcao": self.opcao,
            "data_cadastro": self.data_cadastro.isoformat() if self.data_cadastro else None,
            "ativo": self.ativo
        }

    def build(self):
        return self
