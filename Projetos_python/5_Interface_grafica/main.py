import tkinter as tk

# Funcionalidade para clicar 
def ao_clicar():
    texto = entrada.get()
    rotulo.config(text=texto)

# Criar a janela do sistema 
janela = tk.Tk()

janela.title("Minha primeira janela")

janela.geometry("500x400")

entrada = tk.Entry(janela)
entrada.pack()

# Criar um botão
rotulo = tk.Label(janela, text="Olá Mundo")
rotulo.pack()

botao = tk.Button(janela, text="Clique aqui", command=ao_clicar)
botao.pack()

janela.mainloop()



