import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class EntrevistadoInterface:
    def __init__(self, root, db):
        self.db = db
        self.root = root
        self.root.title("Entrevista")

        # Dicionário com as labels e campos de entrada que desejamos criar
        self.fields = {
            "Nome": None,
            "Email": None,
            "Data de Nascimento": None,
            "Sexo (M/F)": None
        }

        # Criando dinamicamente os labels e campos de entrada
        for index, (label_text, _) in enumerate(self.fields.items()):
            label = tk.Label(root, text=label_text)
            label.grid(row=index, column=0)

            entry = tk.Entry(root)
            entry.grid(row=index, column=1)

            # Salvando as entradas no dicionário para uso posterior
            self.fields[label_text] = entry

        # Botão para iniciar a pesquisa
        self.submit_btn = tk.Button(root, text="Iniciar Pesquisa", command=self.submit)
        self.submit_btn.grid(row=len(self.fields), column=1)

    def submit(self):
        # Captura os valores dos campos de entrada correspondentes
        nome = self.fields["Nome"].get()
        email = self.fields["Email"].get()
        data_nascimento = self.fields["Data de Nascimento"].get()
        sexo = self.fields["Sexo (M/F)"].get()

        if nome and data_nascimento and sexo:
            entrevistado_id = self.db.add_entrevistado(nome, email, data_nascimento, sexo)
            self.respond_perguntas(entrevistado_id)
        else:
            messagebox.showerror("Erro", "Preencha todos os campos")

    def respond_perguntas(self, entrevistado_id):
        pesquisas = self.db.get_pesquisas()
        for pesquisa in pesquisas:
            perguntas = self.db.get_perguntas(pesquisa[0])
            for pergunta in perguntas:
                resposta = simpledialog.askstring("Pergunta", pergunta[2])
                self.db.add_resposta(entrevistado_id, pergunta[0], resposta)
        messagebox.showinfo("Sucesso", "Respostas salvas com sucesso!")
