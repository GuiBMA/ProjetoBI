from datetime import datetime, date
from Entrevistado.genero import Genero

class Entrevistado:

    id_counter = 1
    def __init__(self, nome, email, nome_social, dtNascimento, sexo, genero_id):
        self.id = Entrevistado.id_counter
        Entrevistado.id_counter += 1

        self.set_nome(nome)
        self.set_email(email)
        self.set_nome_social(nome_social)
        self.set_dtNascimento(dtNascimento)
        self.set_sexo(sexo)
        self.set_genero_id(genero_id)
        self.data_cadastro = datetime.now()
    
    def set_nome(self, nome):
        if not nome or len(nome) > 256:
            raise ValueError("nome é obrigatório e deve ter no máximo 256 caracteres.")
        self.nome = nome

    def set_email(self, email):
        if email and len(email) > 128:
            raise ValueError("email deve ter no máximo 128 caracteres.")
        self.email = email

    def set_nome_social(self, nome_social):
        if nome_social and len(nome_social) > 32:
            raise ValueError("nome_social deve ter no máximo 32 caracteres.")
        self.nome_social = nome_social

    def set_dtNascimento(self, dtNascimento):
        if not isinstance(dtNascimento, datetime.date):
            raise ValueError("dtNascimento deve ser uma data válida.")
        self.dtNascimento = date.dtNascimento

    def set_sexo(self, sexo):
        if sexo not in ['M', 'F', 'O']:  # Assuming 'M', 'F', 'O' for Male, Female, Other
            raise ValueError("sexo deve ser 'M', 'F', ou 'O'.")
        self.sexo = sexo

    def set_genero_id(self, genero_id):
        if not isinstance(genero_id, int):
            raise ValueError("genero_id deve ser um número inteiro.")
        self.genero_id = Genero.genero_id

    def to_dict(self):
        """Convert the object to a dictionary for easy serialization."""
        return {
            'id': self.id,
            "nome": self.nome,
            "email": self.email,
            "nome_social": self.nome_social,
            "dtNascimento": self.dtNascimento.isoformat(),
            "sexo": self.sexo,
            "genero_id": self.genero_id,
            "data_cadastro": self.data_cadastro.isoformat(),
        }
