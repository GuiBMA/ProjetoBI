class Genero:
    id_counter = 1

    def __init__(self, genero):
        self.id = Genero.id_counter
        Genero.id_counter += 1

        self.set_genero(genero)
    
    def set_genero(self, genero):
        if not genero or len(genero) > 128:
            raise ValueError("genero é obrigatório e deve ter no máximo 128 caracteres.")
        self.genero = genero
    
    def to_dict(self):
        """Convert the object to a dictionary for easy serialization."""
        return {
            "id": self.id,
            "genero": self.genero,
        }

