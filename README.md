Gerenciador de Tarefas (Python + Tkinter)
Este é um projeto simples de gerenciador de tarefas feito em Python. Ele possui uma interface gráfica básica usando Tkinter, e armazena as tarefas localmente em um arquivo .json, criado automaticamente na mesma pasta do programa.

Funcionalidades
Interface gráfica simples e intuitiva (Tkinter)

Criação automática do arquivo tarefas.json

Adição de novas tarefas

Listagem de tarefas com status (✅ Concluída ou ❌ Pendente)

Marcação de tarefas como concluídas com um clique

Armazenamento local (JSON)

Tecnologias utilizadas
Python 3

Tkinter (interface gráfica)

Bibliotecas padrão: json, os, pathlib

Como executar
Clone o repositório:

bash
Copy
Edit
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Execute o programa:

bash
Copy
Edit
python gerenciador_tarefas.py
Interface gráfica
A aplicação abre uma janela com os seguintes elementos:

Campo de texto para inserir uma nova tarefa

Botão "Adicionar Tarefa"

Lista de tarefas exibidas com status

Botão "Concluir" ao lado de cada tarefa

Tudo é salvo automaticamente no arquivo tarefas.json localizado na mesma pasta do programa.

Estrutura do arquivo tarefas.json
json
Copy
Edit
[
  {
    "nome": "Estudar Python",
    "Concluída": false
  }
]
Licença
Este projeto está licenciado sob a licença MIT.

## Autor

- Raul Netto
