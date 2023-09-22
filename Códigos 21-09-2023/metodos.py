def conexaoBase(lista):
    try:
        leitor = open('inscricoes.dat', 'r')
        for linha in leitor:
            listaSplit=linha.split(';')
            lista.append(listaSplit[0])
        leitor.close()
    except:
        pass

def exibirMenu():
    print("1. Fazer inscrição")
    print("2. Listar inscritos")
    print("3. Registrar entrada no evento")
    print("4. Registrar saída do evento")
    print("5. Sair")

    opcao=input("Opção: ")

    return opcao

def fazerInscricao(lista):
    matricula=input("Informe a matricula:\n")
    if matricula in lista:
        print("Matricula já registrada!")
    else:
        lista.append(matricula)
        nome=input("Informe o nome completo:\n")
        nome=nome.upper()
        email=input("Informe o e-mail:\n")
        email=email.lower()
        escritor=open('inscricoes.dat', 'a', encoding='utf8')
        escritor.write(matricula + ';' + nome + ';' + email + '\n')
        escritor.close()
    
def listarInscritos():
    try:
        leitor = open('inscricoes.dat', 'r', encoding='utf8')
        for linha in leitor:
            listaSplit=linha.split(';')
            print("Nome: ", listaSplit[1], "Matricula: ", listaSplit[0])
    except:
        pass
    
    
# def registrarEntrada():

# def registrarSaida():

