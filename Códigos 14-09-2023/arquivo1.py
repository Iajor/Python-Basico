#criar um programa ou um método que abra, leia, e mostre o conteúdo de um arquivo

while True:
    try:
        nomeArquivo=input("Informe o nome do arquivo:")
        leitor=open(nomeArquivo, 'r', encoding='utf-8')
        print("Arquivo localizado com sucesso.\n")
        
        for linha in leitor:
            linha=linha.replace('\n','')
            print(linha)

        leitor.close()
        break
    except:
        print("Problema para localizar ou abrir o arquivo.\n")