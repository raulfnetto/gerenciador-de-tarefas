import json
import os
from pathlib import Path

caminho = Path(__file__).parent / "tarefas.json"

def criar_arquivo():
    if not caminho.exists():
        with open(caminho, "w") as arquivo:
            json.dump([], arquivo)
            print(f"Arquivo 'tarefas.json' criado na pasta do programa.")
    else:
        print(f"Arquivo 'tarefas.json' já existe.")

def listar_tarefas():
    with open(caminho, "r") as arquivo:
        tarefas = json.load(arquivo)

        if not tarefas:
            print("Nenhuma tarefa cadastrada.\n")
        else:
            for i, tarefa in enumerate(tarefas):
                status = "✅" if tarefa["Concluída"] else "❌"
                print(f"{i+1}. {tarefa['nome']} [{status}]")

def adicionar_tarefa():
    nome_tarefa = input("Digite o nome da tarefa: ")
    nova_tarefa = {
        "nome": nome_tarefa,
        "Concluída": False
    }

    with open(caminho, 'r') as arquivo:
        tarefas = json.load(arquivo)

    tarefas.append(nova_tarefa)

    with open(caminho, 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

    print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")

def marcar_concluida():
    listar_tarefas()
    try:
        tarefa_num = int(input("\nDigite o número da tarefa concluída: "))
        with open(caminho, 'r') as arquivo:
            tarefas = json.load(arquivo)

        if 1 <= tarefa_num <= len(tarefas):
            tarefas[tarefa_num - 1]["Concluída"] = True

            with open(caminho, 'w') as arquivo:
                json.dump(tarefas, arquivo, indent=4)

            print(f"Tarefa '{tarefas[tarefa_num - 1]['nome']}' marcada como concluída!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")

def menu():
    while True:
        print("-------- Gerenciador de Tarefas --------")
        print("\n1 - Listar Tarefas")
        print("2 - Adicionar nova tarefa")
        print("3 - Marcar tarefa como concluída")
        print("4 - Sair")
        print("----------------------------------------")
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            listar_tarefas()
        elif opcao == '2':
            adicionar_tarefa()
        elif opcao == '3':
            marcar_concluida()
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")

criar_arquivo()
menu()
