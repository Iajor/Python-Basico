# Atividade 1)

# seleção

# repetição

# string

# lista

# Construir um Menu com operações: Menu 1 - Cadastrar funcionário 2 - Listar funcionários 3 - Excluir funcionários Opção:

# No programa, o usuário irá digitar, obrigatoriamente, um nome completo. O programa, a partir desse nome, vai gerar seu email com @ufn.edu.br. Por exemplo, Alexandre Zamberlan -> alexandre.zamberlan@ufn.edu.br. Próximo passo, este email deve ser inserido em uma lista que deve controlar duplicados. Na opção 3, o usuário deve digitar o email a ser excluído.
import os

funcionarios={}

while(True):
    os.system('cls')
    print("MENU")
    opcao=input("1-Cadastrar funcionário\n2-Listar funcionários\n3-Excluir funcionários\nOpção:")

    if (opcao == "1"):
        nomeCompleto=input("Informe o nome completo do funcionário\n")
        validaNome=nomeCompleto.split()
        
        if (len(validaNome)>1):
            email=validaNome[0]+'.'+validaNome[-1]+("@ufn.edu.br")
            email=email.lower()
            funcionarios[nomeCompleto]=email
        else:
            print("Informe um nome válido com pelo menos um sobrenome\n")   
    elif (opcao == "2"):
        ordenado=dict(sorted(funcionarios.items()))
        print(ordenado)

    elif (opcao == "3"):
        remove=input("Informe qual registro gostaria de excluir\n")
        del funcionarios[remove]
        print(funcionarios)
    
    if (opcao not in ['1','2','3']):
        print("Informe uma opção válida!")
        
    
    os.system('pause')
