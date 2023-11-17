from classes import Noticia

def exibirMenu():
    print("1. Cadastrar notícia")
    print("2. Alterar notícia")
    print("3. Pesquisar notícia")
    print("4. Remover notícia")
    print("5. Sair")

    opcao=input("Opção: ")

    return opcao

def conexaoBase(lista):
    try:
        leitor = open('noticias.csv', 'r')

        for linha in leitor:
            listaSplit=linha.split(';')
            lista.append(Noticia(listaSplit[0], listaSplit[1], listaSplit[2], listaSplit[3], listaSplit[4], listaSplit[5]))
        leitor.close()
    except:
        pass

def cadastrarNoticia(lista):
    titulo=input("Informe o título da notícia:\n")
    titulo=titulo.upper()
    if titulo in lista:
        print("Notícia já registrada!")
    else:
        lista.append(titulo)
        categoria=input("Informe a categoria da notícia:\n")
        categoria=categoria.upper()
        texto=input("Informe o texto da notícia:\n")
        texto=texto.upper()
        print("Informe 3 palavras chave")
        palavrasChave=[]
        for i in range(3):
            palavra=input("Informe uma palavra chave\n")
            palavrasChave.append(palavra)
        escritor=open('noticias.csv', 'a', encoding='utf8')
        escritor.write(titulo + ';' + categoria + ';' + texto + ';' + palavrasChave[0] + ';' + palavrasChave[1] + ';' + palavrasChave[2] + '\n')
        escritor.close()