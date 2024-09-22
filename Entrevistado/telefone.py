from datetime import datetime

class EntrevistadoTelefone:
    id_counter = 1

    def __init__(self, entrevistado_id, ddd, telefone, tipo, ddi=55, eh_telefone_principal=True, ativo=True):
        self.id = EntrevistadoTelefone.id_counter
        EntrevistadoTelefone.id_counter += 1

        self.set_entrevistado_id(entrevistado_id)
        self.set_ddi(ddi)
        self.set_ddd(ddd)
        self.set_telefone(telefone)
        self.set_tipo(tipo)
        self.eh_telefone_principal = eh_telefone_principal
        self.data_cadastro = datetime.now()
        self.ativo = ativo

    def set_entrevistado_id(self, entrevistado_id):
        if not isinstance(entrevistado_id, int):
            raise ValueError("entrevistado_id deve ser um número inteiro.")
        self.entrevistado_id = entrevistado_id

    def set_ddi(self, ddi):
        if not isinstance(ddi, int) or ddi <= 0:
            raise ValueError("ddi deve ser um número inteiro positivo.")
        self.ddi = ddi

    def set_ddd(self, ddd):
        if not isinstance(ddd, int) or len(str(ddd)) != 2:
            raise ValueError("ddd deve ser um número inteiro de 2 dígitos.")
        self.ddd = ddd

    def set_telefone(self, telefone):
        if not isinstance(telefone, int) or len(str(telefone)) not in [8, 9]:
            raise ValueError("telefone deve ser um número inteiro de 8 ou 9 dígitos.")
        self.telefone = telefone


        if not isinstance(telefone_tipo_id, int):
            raise ValueError("telefone_tipo_id deve ser um número inteiro.")
        self.telefone_tipo_id = telefone_tipo_id

    def set_tipo(self, tipo):
        if not tipo or len(tipo) > 32:
            raise ValueError("Tipo é obrigatório e deve ter no máximo 32 caracteres.")
        self.tipo = tipo

    def to_dict(self):
        return {
            "id": self.id,
            "entrevistado_id": self.entrevistado_id,
            "ddi": self.ddi,
            "ddd": self.ddd,
            "telefone": self.telefone,
            "tipo": self.tipo,
            "eh_telefone_principal": self.eh_telefone_principal,
            "data_cadastro": self.data_cadastro.isoformat(),
            "ativo": self.ativo
        }
