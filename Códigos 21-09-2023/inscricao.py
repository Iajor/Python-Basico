import os
import metodos


listaMatricula = []
metodos.conexaoBase(listaMatricula)

while(True):
    os.system('cls')
    opcao=metodos.exibirMenu()

    if opcao == '1':
        metodos.fazerInscricao(listaMatricula)

    elif opcao == '2':
        metodos.listarInscritos()

    elif opcao == '3':
        metodos.registrarEntrada()

    elif opcao == '4':
        metodos.registrarSaida()

    elif opcao == '5':
        print("Finalizando...")
        break

    else:
        print("Opcão inválida! Informe um opção válida.")
    
    os.system('pause')