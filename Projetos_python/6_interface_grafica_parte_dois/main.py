import tkinter as tk

def ao_clicar():
    texto = entrada.get()
    rotulo.config(text=texto)

janela = tk.Tk()
janela.title("Organizando com Frames")
janela.geometry("500x800")

frame_superior = tk.Frame(janela)
frame_superior.pack()

frame_inferiror = tk.Frame(janela)
frame_inferiror.pack()

rotulo = tk.Label(frame_superior, text="Digite algo e clique no botão")
rotulo.pack()

entrada = tk.Entry(frame_superior)
entrada.pack()

botao = tk.Button(frame_inferiror, text="Clique aqui", command=ao_clicar)
botao.pack()

janela.mainloop()

