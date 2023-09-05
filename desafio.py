# Desafio 2)
# Fazer programa em Python que tenha um Menu com as opções abaixo. Entretanto, para cada opção, criar um método (módulo) específico.

# Menu

# Cadastrar placa na lista (validar se a placa já foi cadastrada e se tem o tamanho de caracteres obrigatórios)
# Mostrar placas cadastradas (de forma ordenada)
# Remover placa da lista
# Sair
# Opção:

def exibirMenu():
    
    print("\nMenu:")
    print("1. Cadastrar placa na lista")
    print("2. Mostrar placas cadastradas")
    print("3. Remover placa da lista")
    print("4. Sair")

    opcao = input("Opção: ")
    return opcao

def cadastrarPlaca(placas):
    placa = input("Digite a placa a ser cadastrada: ")

    if len(placa) != 7:
        print("A placa deve ter 7 caracteres.")
    elif placa in placas:
        print("Essa placa já foi cadastrada.")
    else:
        placas.append(placa)
        print("Placa cadastrada com sucesso!")

def mostrarPlacas(placas):
    placas.sort()
    print("\nPlacas cadastradas:")
    for placa in placas:
        print(placa)

def removerPlaca(placas):
    placa = input("Digite a placa a ser removida: ")
    if placa in placas:
        placas.remove(placa)
        print("Placa removida com sucesso!")
    else:
        print("Placa não encontrada na lista.")


placas = [] 

while True:
    
    opcao = exibirMenu()

    if opcao == "1":
        cadastrarPlaca(placas)
    elif opcao == "2":
        mostrarPlacas(placas)
    elif opcao == "3":
        removerPlaca(placas)
    elif opcao == "4":
        print("Encerrando...")
        break
    else:
        print("Opção inválida. Insira uma opção válida.")




