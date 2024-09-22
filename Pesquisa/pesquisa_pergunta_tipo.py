from datetime import datetime

class PesquisaPerguntaTipo:

    id_counter = 1
    def __init__(self):
        self.id = PesquisaPerguntaTipo.id_counter
        PesquisaPerguntaTipo.id_counter += 1

        self.tipo = None
        self.data_cadastro = None
        self.ativo = True


        self.tipo_id = tipo_id
        return self

    def set_tipo(self, tipo):
        self.tipo = tipo
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
            "tipo": self.tipo,
            "data_cadastro": self.data_cadastro.isoformat() if self.data_cadastro else None,
            "ativo": self.ativo
        }

    def build(self):
        return self
