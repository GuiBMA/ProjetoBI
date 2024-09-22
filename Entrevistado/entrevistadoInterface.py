import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from Entrevistado.entrevistado import Entrevistado
from dataBase import Database
class EntrevistadoInterface:
    def __init__(self, root, db, entrevistado):
        entrevistado = entrevistado
        self.db = db
        self.root = root
        self.root.title("Entrevista")
        self.fields = {
            "Nome": None,
            "Email": None,
            "Data de Nascimento": None,
            "Sexo (M/F)": None
        }

        for index, (label_text, _) in enumerate(self.fields.items()):
            label = tk.Label(root, text=label_text)
            label.grid(row=index, column=0)
            entry = tk.Entry(root)
            entry.grid(row=index, column=1)
            self.fields[label_text] = entry

        self.submit_btn = tk.Button(root, text="Iniciar Pesquisa", command=self.submit)
        self.submit_btn.grid(row=len(self.fields), column=1)

    def submit(self):
        nome = self.fields["Nome"].get()
        email = self.fields["Email"].get()
        data_nascimento = self.fields["Data de Nascimento"].get()
        sexo = self.fields["Sexo (M/F)"].get()

        if nome and data_nascimento and sexo:
            try:
                entrevistado = Entrevistado(nome, email, None, data_nascimento, sexo, None)
                entrevistado_id = Database.add_entrevistado(entrevistado)
                self.respond_perguntas(entrevistado_id)
            except ValueError as e:
                messagebox.showerror("Erro", str(e))
        else:
            messagebox.showerror("Erro", "Preencha todos os campos")

    def respond_perguntas(self, entrevistado_id):
        pesquisas = Database.get_pesquisas()
        for pesquisa in pesquisas:
            perguntas = Database.get_perguntas(pesquisa[0])
            for pergunta in perguntas:
                resposta = simpledialog.askstring("Pergunta", pergunta[2])
                Database.add_resposta(entrevistado_id, pergunta[0], resposta)
        messagebox.showinfo("Sucesso", "Respostas salvas com sucesso!")
