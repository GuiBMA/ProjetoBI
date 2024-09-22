import tkinter as tk
from admin import AdminInterface
from Entrevistado.entrevistadoInterface import EntrevistadoInterface
from dataBase import Database
import Serializer
def load_interface(choice, root, db, serializer):
    if choice == '1':
        print("Carregando a interface do Admin...")
        AdminInterface(root, db, serializer)
    elif choice == '2':
        print("Carregando a interface do Entrevistado...")
        EntrevistadoInterface(root, db, serializer)

if __name__ == "__main__":
    db = Database()
    serializer = Serializer.Serializer()

    
    while True:
        root = tk.Tk()
        choice = input("Escolha a interface: (1) Admin, (2) Entrevistado, ou (0) Sair: ")
        
        if choice == '0':
            print("Saindo do programa...")
            serializer.serialize()
            break

        
        if choice in ['1', '2']:
            load_interface(choice, root, db, serializer)
            root.mainloop()
            print("Voltando ao menu inicial...")
        else:
            print("Escolha inválida. Tente novamente.")