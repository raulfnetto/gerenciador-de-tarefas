import json
import os
from pathlib import Path



def criar_arquivo():
    desktop = Path(os.path.expanduser("~")) / "OneDrive" / "Área de Trabalho" / "tarefas.json"

    if not os.path.exists(desktop):
        with open(desktop, "w") as arquivo:
            json.dump([], arquivo)
            print(f"Arquivo 'tarefas.json' criado na Área de Trabalho.")
    else:
        print(f"Arquivo 'tarefas.json' já existe na Área de Trabalho.")



def listar_tarefas():
    caminho = Path(os.path.expanduser("~")) / "OneDrive" / "Área de Trabalho" / "tarefas.json"
    with open(caminho, "r") as arquivo:
        tarefas = json.load(arquivo)

        if not tarefas:
            print("Nenhuma tarefa cadastrada.\n\n")
        else:
            for i, tarefa in enumerate(tarefas):
                status = "✅" if tarefa["Concluída"] else "❌"
                print(f"{i+1}. {tarefa['nome']} [{status}]")



def adicionar_tarefa():
    caminho = Path(os.path.expanduser("~")) / "OneDrive" / "Área de Trabalho" / "tarefas.json"
    nome_tarefa = input("Por favor, insira o nome da tarefa que deseja adicionar: ")
    nova_tarefa = {
        "nome": nome_tarefa,
        "Concluída": False
    }

    with open(caminho, 'r') as arquivo:
        tarefas = json.load(arquivo)

        tarefas.append(nova_tarefa)

        with open(caminho, 'w') as arquivo:
            json.dump(tarefas, arquivo, indent = 4)

        print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")


def marcar_concluida():
    caminho = Path(os.path.expanduser("~")) / "OneDrive" / "Área de Trabalho" / "tarefas.json"
    listar_tarefas()
    try:
        tarefa_num = int(input("\nDigite o número da tarefa que deseja marcar como concluída: "))
        with open(caminho, 'r') as arquivo:
            tarefas = json.load(arquivo)

        if 1 <= tarefa_num <= len(tarefas):
            tarefas[tarefa_num - 1]["Concluída"] = True 

            with open(caminho, 'w') as arquivo:
                json.dump(tarefas, arquivo, indent=4)

            print(f"Tarefa '{tarefas[tarefa_num - 1]['nome']}' marcada como concluída!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")



def menu():

    while True:
        print("-------- Gerenciador de Tarefas --------")
        print("\n1 - Listar Tarefas")
        print("2 - Adicionar nova tarefa")
        print("3 - Marcar tarefa como concluída")
        print("4 - Sair")
        print("----------------------------------------")
        opcao = input("\nPor favor, digite qual opção você deseja executar: ")

        if opcao == '1':
            listar_tarefas()

        if opcao == '2':
            adicionar_tarefa()

        if opcao == '3':
            marcar_concluida()

        if opcao == '4':
            break

criar_arquivo()

menu()