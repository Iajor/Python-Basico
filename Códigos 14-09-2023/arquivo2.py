

listaEmail=[]

while True:
    try:
        nomeArquivo=input("Informe o arquivo .dat:\n")
        leitor=open(nomeArquivo,'r',encoding='utf8')

        for linha in leitor:
            vetorLinha=linha.split(';')
            listaEmail.append(vetorLinha[1])
        
        leitor.close()
        listaEmail.sort()
        print(listaEmail)
        break
    except:
        print("deu erro")