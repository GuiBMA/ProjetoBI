import tkinter as tk
from admin import AdminInterface
from dataBase import Database

if __name__ == "__main__":
    db = Database()
    
    root = tk.Tk()
    
    # Escolha qual interface carregar (Admin ou Entrevistado)
    AdminInterface(root, db)

    # EntrevistadoInterface(root, db)
    root.mainloop()