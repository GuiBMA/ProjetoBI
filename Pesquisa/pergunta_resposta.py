from datetime import datetime

class PerguntaResposta:
    id_counter = 1
    def __init__(self):
        self.id = PerguntaResposta.id_counter
        PerguntaResposta.id_counter += 1

        self.pesquisa_pergunta_id = None
        self.entrevistado_id = None
        self.resposta = None
        self.data_cadastro = None

    def set_pesquisa_pergunta_id(self, pesquisa_pergunta_id):
        self.pesquisa_pergunta_id = pesquisa_pergunta_id
        return self

    def set_entrevistado_id(self, entrevistado_id):
        self.entrevistado_id = entrevistado_id
        return self

    def set_resposta(self, resposta):
        self.resposta = resposta
        return self

    def set_data_cadastro(self, data_cadastro: datetime = None):
        self.data_cadastro = data_cadastro or datetime.now()
        return self

    def to_dict(self):
        return {
            "id": self.id,
            "pesquisa_pergunta_id": self.pesquisa_pergunta_id,
            "entrevistado_id": self.entrevistado_id,
            "resposta": self.resposta,
            "data_cadastro": self.data_cadastro.isoformat() if self.data_cadastro else None
        }

    def build(self):
        return self
