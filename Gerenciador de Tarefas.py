import json
import os
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

caminho = Path(__file__).parent / "tarefas.json"

def criar_arquivo():
    if not caminho.exists():
        with open(caminho, "w") as f:
            json.dump([], f)

def carregar_tarefas():
    with open(caminho, "r") as f:
        return json.load(f)

def salvar_tarefas(tarefas):
    with open(caminho, "w") as f:
        json.dump(tarefas, f, indent=4)

def atualizar_lista():
    tarefas = carregar_tarefas()
    lista.delete(*lista.get_children())
    for i, tarefa in enumerate(tarefas):
        status = "Concluída" if tarefa["Concluída"] else "Pendente"
        lista.insert("", "end", iid=i, values=(tarefa["nome"], status))

def adicionar():
    nome = simpledialog.askstring("Nova Tarefa", "Digite o nome da tarefa:")
    if nome:
        tarefas = carregar_tarefas()
        tarefas.append({"nome": nome, "Concluída": False})
        salvar_tarefas(tarefas)
        atualizar_lista()

def marcar_concluida():
    selecionado = lista.focus()
    if selecionado:
        tarefas = carregar_tarefas()
        tarefas[int(selecionado)]["Concluída"] = True
        salvar_tarefas(tarefas)
        atualizar_lista()
    else:
        messagebox.showwarning("Aviso", "Selecione uma tarefa.")

#Interface
criar_arquivo()
root = tk.Tk()
root.title("Gerenciador de Tarefas")

lista = ttk.Treeview(root, columns=("Nome", "Status"), show="headings")
lista.heading("Nome", text="Tarefa")
lista.heading("Status", text="Status")
lista.pack(padx=10, pady=10, fill="both", expand=True)

frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=5)

tk.Button(frame_botoes, text="Adicionar Tarefa", command=adicionar).pack(side="left", padx=5)
tk.Button(frame_botoes, text="Marcar como Concluída", command=marcar_concluida).pack(side="left", padx=5)

atualizar_lista()
root.mainloop()
