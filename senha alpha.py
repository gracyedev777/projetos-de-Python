import tkinter as tk
from tkinter import messagebox
import random
import string

class CriadorDeSenhas:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Criador de Senhas")
        self.tamanho_label = tk.Label(self.janela, text="Tamanho da senha (pelo menos 8 caracteres sem vogais)")
        self.tamanho_label.pack()
        self.tamanho_entry = tk.Entry(self.janela)
        self.tamanho_entry.pack()
        self.gerar_button = tk.Button(self.janela, text="Gerar Senha", command=self.gerar_senha)
        self.gerar_button.pack()
        self.senha_label = tk.Label(self.janela, text="Senha gerada:")
        self.senha_label.pack()
        self.senha_entry = tk.Entry(self.janela, width=30)
        self.senha_entry.pack()
        self.aviso_label = tk.Label(self.janela, text="Aviso: Use a senha com cuidado")
        self.aviso_label.pack()
        self.aviso_label = tk.Label(self.janela, text="sem direitos autorais kk")
    

    def gerar_senha(self):
        try:
            tamanho = int(self.tamanho_entry.get())
            if tamanho < 8:
                messagebox.showerror("Erro", "O tamanho da senha deve ser pelo menos 8 caracteres burru")
                return
            caracteres = string.ascii_letters + string.digits + "!@#$%^&*()_+-=✯☭"
            senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
            self.senha_entry.delete(0, tk.END)
            self.senha_entry.insert(0, senha)
        except ValueError:
            messagebox.showerror("Erro", "O tamanho da senha deve ser um número mongoloide")

    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    criador = CriadorDeSenhas()
    criador.run()