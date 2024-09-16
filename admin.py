import tkinter as tk
from tkinter import messagebox

class AdminInterface:
    def __init__(self, root, db):
        self.db = db
        self.root = root
        self.root.title("Administração de Pesquisas")

        # Dicionário com as labels e os campos de entrada que desejamos criar
        self.fields = {
            "Nome da Pesquisa": None,
            "Data de Início": None,
            "Data de Fim": None,
            "ID da Pesquisa": None,
            "Pergunta": None
        }

        # Criando dinamicamente os labels e campos de entrada
        for index, (label_text, _) in enumerate(self.fields.items()):
            label = tk.Label(root, text=label_text)
            label.grid(row=index, column=0)
            
            entry = tk.Entry(root)
            entry.grid(row=index, column=1)
            
            # Salvando as entradas no dicionário para uso posterior
            self.fields[label_text] = entry

        # Botão para adicionar pesquisa
        self.add_pesquisa_btn = tk.Button(root, text="Adicionar Pesquisa", command=self.add_pesquisa)
        self.add_pesquisa_btn.grid(row=len(self.fields), column=1)

        # Botão para adicionar pergunta
        self.add_pergunta_btn = tk.Button(root, text="Adicionar Pergunta", command=self.add_pergunta)
        self.add_pergunta_btn.grid(row=len(self.fields) + 1, column=1)

    def add_pesquisa(self):
        # Captura os valores dos campos de entrada correspondentes
        nome = self.fields["Nome da Pesquisa"].get()
        data_inicio = self.fields["Data de Início"].get()
        data_fim = self.fields["Data de Fim"].get()

        if nome and data_inicio and data_fim:
            self.db.add_pesquisa(nome, data_inicio, data_fim)
            messagebox.showinfo("Sucesso", "Pesquisa adicionada com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos")

    def add_pergunta(self):
        pesquisa_id = self.fields["ID da Pesquisa"].get()
        pergunta_texto = self.fields["Pergunta"].get()

        if pesquisa_id and pergunta_texto:
            self.db.add_pergunta(pesquisa_id, pergunta_texto)
            messagebox.showinfo("Sucesso", "Pergunta adicionada com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos")

