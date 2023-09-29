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
       
def registrarEntrada(lista):
    matricula=input("Informe a matricula:\n")
    if matricula not in lista:
        print("Participante não está inscrito no evento!")
    else:
        try:
            escritor=open('entrada.dat', 'a', encoding='utf8')
            horaEntrada=input("Informe o horário de entrada:")
            escritor.write(matricula+';'+horaEntrada+'\n')
            escritor.close()
            print("Entrada registrada!")
        except:
            pass

def registrarSaida():
    listaEntrada=[]
    listaSaida=[]

    try:
        leitor=open('entrada.dat', 'r', encoding='utf8')
        for linha in leitor:
            listaSplit=linha.split(';')
            listaEntrada.append(listaSplit[0])
            
        leitor.close()

    except:
        print("Deu erro!")
    
    try:
        leitor=open('saida.dat', 'r', encoding='utf8')
        for linha in leitor:
            listaSplit=linha.split(';')
            listaSaida.append(listaSplit[0])
            
        leitor.close()

    except:
        print("Deu erro!")

    matricula=input("Informe a matricula:")
    
    if matricula in listaSaida:
        print("Participante já saiu!")

    else:
        if matricula not in listaEntrada:
            print("Participante não entrou no evento!")
        else:
            try:
                escritor=open('saida.dat', 'a', encoding='utf8')
                horaSaida=input("Informe o horário de saída:")
                escritor.write(matricula+';'+horaSaida+'\n')
                escritor.close()
                print("Saída registrada!")
            except:
                pass

    
   
    # strEntrada=horaEntrada.split(':')
    # intEntrada=(int(strEntrada[0])*60)+(int(strEntrada[1]))
    # strSaida=horaSaida.split(':')
    # intSaida=(int(strSaida[0])*60)+(int(strSaida[1]))
    # totalTempo=intSaida-intEntrada

    # if totalTempo >= 60:
    #     print("Seu certificado será encaminhado pelo e-mail")
    # else:
    #     print("Participante não receberá certificado, pois o tempo de permanência foi insuficiente.")
