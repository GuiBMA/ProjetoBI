class Endereco:

    id_counter = 1
    def __init__(self, entrevistado_id, logradouro, numero, bairro, cidade, uf, cep, complemento=None, descricao=None):
        self.id = Endereco.id_counter
        Endereco.id_counter += 1
        
        self.set_entrevistado_id(entrevistado_id)
        self.set_logradouro(logradouro)
        self.set_numero(numero)
        self.set_bairro(bairro)
        self.set_cidade(cidade)
        self.set_uf(uf)
        self.set_cep(cep)
        self.set_complemento(complemento)
        self.set_descricao(descricao)
    
    def set_entrevistado_id(self, entrevistado_id):
        if not entrevistado_id or len(entrevistado_id) > 256:
            raise ValueError("ID do entrevistado.")
        self.entrevistado_id = entrevistado_id

    def set_logradouro(self, logradouro):
        if not logradouro or len(logradouro) > 256:
            raise ValueError("logradouro é obrigatório e deve ter no máximo 256 caracteres.")
        self.logradouro = logradouro
    
    def set_numero(self, numero):
        if not numero or len(numero) > 64:
            raise ValueError("numero é obrigatório e deve ter no máximo 64 caracteres.")
        self.numero = numero
    
    def set_complemento(self, complemento):
        if complemento and len(complemento) > 256:
            raise ValueError("complemento deve ter no máximo 256 caracteres.")
        self.complemento = complemento
    
    def set_bairro(self, bairro):
        if not bairro or len(bairro) > 256:
            raise ValueError("bairro é obrigatório e deve ter no máximo 256 caracteres.")
        self.bairro = bairro
    
    def set_cidade(self, cidade):
        if not cidade or len(cidade) > 256:
            raise ValueError("cidade é obrigatória e deve ter no máximo 256 caracteres.")
        self.cidade = cidade
    
    def set_uf(self, uf):
        if not uf or len(uf) != 2:
            raise ValueError("uf é obrigatório e deve ter exatamente 2 caracteres.")
        self.uf = uf.upper()
    
    def set_cep(self, cep):
        if not cep or len(cep) != 8:
            raise ValueError("cep é obrigatório e deve ter exatamente 8 caracteres.")
        self.cep = cep
    
    def set_descricao(self, descricao):
        if descricao and len(descricao) > 32:
            raise ValueError("descricao deve ter no máximo 32 caracteres.")
        self.descricao = descricao
    
    def to_dict(self):
        return {
            "id": self.id,
            "entrevistado_id": self.entrevistado_id,
            "logradouro": self.logradouro,
            "numero": self.numero,
            "complemento": self.complemento,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "uf": self.uf,
            "cep": self.cep,
            "descricao": self.descricao,
        }
