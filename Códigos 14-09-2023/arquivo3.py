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

        escritor=open('emails.dat','w')
        for email in listaEmail:
            escritor.write(email+'\n')
        
        escritor.close()
        
        break
    except:
        print("deu erro")