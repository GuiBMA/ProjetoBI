import unittest
from unittest.mock import MagicMock, patch
from tkinter import Tk
from admin import AdminInterface
from entrevistado import EntrevistadoInterface

class Testes(unittest.TestCase):
    def setUp(self):
        self.root = Tk()  # Criamos um root do Tkinter para ser usado nos testes
        self.mock_db = MagicMock()  # Criamos um mock para simular o banco de dados

        # Instâncias das interfaces que serão testadas
        self.admin_interface = AdminInterface(self.root, self.mock_db)
        self.entrevistado_interface = EntrevistadoInterface(self.root, self.mock_db)

    # Testes para AdminInterface
    def test_add_pesquisa_success(self):
        # Simulamos as entradas do formulário
        self.admin_interface.fields["Nome da Pesquisa"].insert(0, "Pesquisa Teste")
        self.admin_interface.fields["Data de Início"].insert(0, "2024-09-01")
        self.admin_interface.fields["Data de Fim"].insert(0, "2024-12-01")

        # Executamos o método a ser testado
        self.admin_interface.add_pesquisa()

        # Verificamos se o método add_pesquisa foi chamado com os parâmetros corretos
        self.mock_db.add_pesquisa.assert_called_once_with("Pesquisa Teste", "2024-09-01", "2024-12-01")

    def test_add_pesquisa_missing_fields(self):
        # Simulamos apenas parte dos campos preenchidos
        self.admin_interface.fields["Nome da Pesquisa"].insert(0, "Pesquisa Teste")

        with patch('tkinter.messagebox.showerror') as mock_error:
            # Executamos o método a ser testado
            self.admin_interface.add_pesquisa()

            # Verificamos se a caixa de erro foi chamada por falta de preenchimento
            mock_error.assert_called_once_with("Erro", "Preencha todos os campos")

    def test_add_pergunta_success(self):
        # Simulamos as entradas do formulário
        self.admin_interface.fields["ID da Pesquisa"].insert(0, "1")
        self.admin_interface.fields["Pergunta"].insert(0, "Qual seu meio de transporte?")

        # Executamos o método a ser testado
        self.admin_interface.add_pergunta()

        # Verificamos se o método add_pergunta foi chamado com os parâmetros corretos
        self.mock_db.add_pergunta.assert_called_once_with("1", "Qual seu meio de transporte?")

    # Testes para EntrevistadoInterface
    def test_submit_success(self):
        # Simulamos as entradas do formulário
        self.entrevistado_interface.fields["Nome"].insert(0, "João Silva")
        self.entrevistado_interface.fields["Email"].insert(0, "joao@example.com")
        self.entrevistado_interface.fields["Data de Nascimento"].insert(0, "1990-01-01")
        self.entrevistado_interface.fields["Sexo (M/F)"].insert(0, "M")

        # Simulamos que o método add_entrevistado retorna um ID
        self.mock_db.add_entrevistado.return_value = 1

        with patch('tkinter.simpledialog.askstring', return_value="Carro"):
            with patch('tkinter.messagebox.showinfo') as mock_info:
                # Executamos o método a ser testado
                self.entrevistado_interface.submit()

                # Verificamos se o método add_entrevistado foi chamado corretamente
                self.mock_db.add_entrevistado.assert_called_once_with(
                    "João Silva", "joao@example.com", "1990-01-01", "M"
                )

                # Verificamos se a mensagem de sucesso foi exibida
                mock_info.assert_called_once_with("Sucesso", "Respostas salvas com sucesso!")

    def test_submit_missing_fields(self):
        # Simulamos entrada incompleta
        self.entrevistado_interface.fields["Nome"].insert(0, "João Silva")

        with patch('tkinter.messagebox.showerror') as mock_error:
            # Executamos o método a ser testado
            self.entrevistado_interface.submit()

            # Verificamos se a caixa de erro foi chamada devido aos campos incompletos
            mock_error.assert_called_once_with("Erro", "Preencha todos os campos")

    def tearDown(self):
        self.root.destroy()  # Fechamos a janela do Tkinter após os testes
