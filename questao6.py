import os
import json

# Função para carregar tarefas a partir do arquivo JSON
def carregar_tarefas():
    if os.path.exists('tarefas.json'): #verifica se o "tarefas.json" existe
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    else:
        return []

# Função para salvar tarefas no arquivo JSON
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

# Função para adicionar uma nova tarefa
def adicionar_tarefa(tarefas, descricao):
    tarefa = {'descricao': descricao, 'concluida': False}
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

# Função para listar tarefas
def listar_tarefas(tarefas):
    for i, tarefa in enumerate(tarefas, start=1):
        descricao = tarefa['descricao'] if 'descricao' in tarefa else "Descrição não encontrada"
        concluida = tarefa['concluida'] if 'concluida' in tarefa else False
        status = 'Concluída' if concluida else 'Pendente'
        print(f'{i}. {descricao} ({status})')


# Função para marcar uma tarefa como concluída
def marcar_como_concluida(tarefas, indice):
    if 1 <= indice <= len(tarefas):
        tarefas[indice - 1]['concluida'] = True
        salvar_tarefas(tarefas)
    else:
        print("Índice inválido.")

# Função para remover uma tarefa
def remover_tarefa(tarefas, indice):
    if 1 <= indice <= len(tarefas):
        tarefas.pop(indice - 1)
        salvar_tarefas(tarefas)
    else:
        print("Índice inválido.")

# Função principal
def main():
    tarefas = carregar_tarefas()

    while True:
        print("\nOpções:")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Marcar como concluída")
        print("4. Remover tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\nTarefas:")
            listar_tarefas(tarefas)
        elif opcao == '2':
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(tarefas, descricao)
        elif opcao == '3':
            print("\nTarefas:")
            listar_tarefas(tarefas)
            indice = int(input("Digite o número da tarefa concluída: "))
            marcar_como_concluida(tarefas, indice)
        elif opcao == '4':
            print("\nTarefas:")
            listar_tarefas(tarefas)
            indice = int(input("Digite o número da tarefa a ser removida: "))
            remover_tarefa(tarefas, indice)
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

