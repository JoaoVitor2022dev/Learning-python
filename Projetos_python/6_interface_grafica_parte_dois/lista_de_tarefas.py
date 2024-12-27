import tkinter as tk

def adicionar_tarefa():
    tarefa = entrada.get()
    if tarefa != "":
        lista_tarefa.insert(tk.END, tarefa)
        entrada.delete(0, tk.END)

def remover_tarefas():
    try:
        indice_selecionado = lista_tarefa.curselection()[0]
        lista_tarefas.delete(indice_selecionado) 
    except: 
        pass
        
