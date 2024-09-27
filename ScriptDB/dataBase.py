import sqlite3

class Database:
    def __init__(self, db_name="pesquisa.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS pesquisa (
                                    pesquisa_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    pesquisa_nome TEXT NOT NULL,
                                    data_inicio TEXT NOT NULL,
                                    data_fim TEXT NOT NULL,
                                    ativo BOOLEAN NOT NULL DEFAULT 1
                                );''')
            
            self.conn.execute('''CREATE TABLE IF NOT EXISTS pesquisa_pergunta (
                                    pesquisa_pergunta_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    pesquisa_id INTEGER,
                                    pergunta_texto TEXT NOT NULL,
                                    FOREIGN KEY (pesquisa_id) REFERENCES pesquisa(pesquisa_id)
                                );''')
            
            self.conn.execute('''CREATE TABLE IF NOT EXISTS entrevistado (
                                    entrevistado_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT NOT NULL,
                                    email TEXT,
                                    data_nascimento TEXT NOT NULL,
                                    sexo TEXT NOT NULL
                                );''')
            
            self.conn.execute('''CREATE TABLE IF NOT EXISTS resposta (
                                    resposta_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    entrevista_id INTEGER,
                                    pergunta_id INTEGER,
                                    resposta TEXT,
                                    FOREIGN KEY (pergunta_id) REFERENCES pesquisa_pergunta(pesquisa_pergunta_id),
                                    FOREIGN KEY (entrevista_id) REFERENCES entrevistado(entrevistado_id)
                                );''')

    def add_pesquisa(self, nome, data_inicio, data_fim):
        with self.conn:
            self.conn.execute("INSERT INTO pesquisa (pesquisa_nome, data_inicio, data_fim) VALUES (?, ?, ?)", 
                              (nome, data_inicio, data_fim))

    def add_pergunta(self, pesquisa_id, pergunta_texto):
        with self.conn:
            self.conn.execute("INSERT INTO pesquisa_pergunta (pesquisa_id, pergunta_texto) VALUES (?, ?)", 
                              (pesquisa_id, pergunta_texto))

    def get_pesquisas(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM pesquisa WHERE ativo=1")
        return cur.fetchall()

    def get_perguntas(self, pesquisa_id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM pesquisa_pergunta WHERE pesquisa_id=?", (pesquisa_id,))
        return cur.fetchall()

    def add_entrevistado(self, nome, email, data_nascimento, sexo):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO entrevistado (nome, email, data_nascimento, sexo) VALUES (?, ?, ?, ?)", 
                        (nome, email, data_nascimento, sexo))
            return cur.lastrowid

    def add_resposta(self, entrevistado_id, pergunta_id, resposta):
        with self.conn:
            self.conn.execute("INSERT INTO resposta (entrevista_id, pergunta_id, resposta) VALUES (?, ?, ?)", 
                              (entrevistado_id, pergunta_id, resposta))

