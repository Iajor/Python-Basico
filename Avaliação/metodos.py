from classes import Noticia

def exibirMenu():
    print("1. Cadastrar notícia")
    print("2. Pesquisar notícia")
    print("3. Alterar notícia")
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

def atualizarArquivo(lista):
    with open('noticias.csv', 'w', encoding='utf8') as escritor:
        for noticia in lista:
            escritor.write(noticia.titulo + ';' + noticia.categoria + ';' + noticia.texto + ';' + noticia.palavrasChave[0] + ';' + noticia.palavrasChave[1] + ';' + noticia.palavrasChave[2])

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
        escritor.write(titulo + ';' + categoria + ';' + texto + ';' + palavrasChave[0]+ ';' + palavrasChave[1] + ';' + palavrasChave[2] +'\n')
        escritor.close()

def pesquisarNoticia(lista):
    pesquisa=input("Informe o que deseja pesquisar na notícia:\n1-Título\n2-Categoria\n3-Texto\n4-Palavras-chave\n5-Voltar\n")
    

    if pesquisa == '1':
        termo=input("Informe o termo de pesquisa no título\n").upper()
        encontrada=False
        for noticia in lista:
            if termo in noticia.titulo:
                encontrada=True
                print(f'A palavra foi encontrada em {noticia.titulo.title()}')
                
        if not encontrada:
            print(f'O termo {termo.title()} não foi localizado nos títulos de notícias cadastradas')
    
    if pesquisa == '2':
        termo=input("Informe o termo de pesquisa na categoria\n").upper()
        encontrada=False
        for noticia in lista:
            if termo in noticia.categoria:
                encontrada=True
                print(f'A palavra foi encontrada em {noticia.categoria.title()}')
                
        if not encontrada:
            print(f'O termo {termo.title()} não foi localizado nas categorias de notícias cadastradas')
    
    if pesquisa == '3':
        termo=input("Informe o termo de pesquisa no texto\n").upper()
        encontrada=False
        for noticia in lista:
            if termo in noticia.texto:
                encontrada=True
                print(f'A palavra foi encontrada em {noticia.texto}')
                
        if not encontrada:
            print(f'O termo {termo} não foi localizado nos textos de notícias cadastradas')
    
    if pesquisa == '4':
        termo=input("Informe o termo de pesquisa nas palavras-chaves\n")
        encontrada=False
        for noticia in lista:
            palavrasChaves=[noticia.palavrasChave[0],noticia.palavrasChave[1],noticia.palavrasChave[2].rstrip('\n')]
            if termo in palavrasChaves:
                encontrada=True
                print(f'A palavra foi encontrada na notícia de título {noticia.titulo.title()}')
                
        if not encontrada:
            print(f'O termo {termo} não foi localizado nos textos de notícias cadastradas')
    
def alterarNoticia(lista):

    noticiaAlteracao=input("Informe o titulo da noticia a ser a alterada:\n").upper()
    encontrei=False
    for noticia in lista:
        if noticiaAlteracao in noticia.titulo:
            encontrei = True
            alteracao=input("Informe o que deseja alterar na notícia:\n1-Título\n2-Categoria\n3-Texto\n4-Palavras-chave\n5-Voltar\n")    
            if alteracao == '1':
                novoTitulo = input("Informe o novo título\n").upper()
                noticia.titulo = novoTitulo
                atualizarArquivo(lista)
                print('Título alterado com sucesso!')
                 
            if alteracao == '2':
                print(f'A categoria desta notícia é {noticia.categoria.title()}')
                novaCategoria = input("Informe a nova categoria\n").upper()
                noticia.categoria = novaCategoria 
                atualizarArquivo(lista)
                print('Categoria alterada com sucesso!')
            
            if alteracao == '3':
                print(f'O texto desta notícia é {noticia.texto}')
                novoTexto = input("Informe o novo texto\n").upper()
                noticia.texto = novoTexto
                atualizarArquivo(lista)
                print('Texto alterado com sucesso!')
                        
            if alteracao == '4':
                print(f'As palavras-chaves desta notícia são {noticia.palavrasChave[0]},{noticia.palavrasChave[1]},{noticia.palavrasChave[2]}')
                palavrasChaves=[]
                for i in range(3):
                    palavra=input("Informe as novas palavras-chave\n")
                    palavrasChaves.append(palavra)
                noticia.palavrasChave = palavrasChaves
                atualizarArquivo(lista)
                print('Palavras-chave alteradas com sucesso!')
            if alteracao == '5':
                break
    if not encontrei:
        print("Notícia não encontrada!")

def removerNoticia(lista):
    noticiaRemocao=input("Informe o titulo da noticia a ser a removida:\n").upper()
    encontrei=False
    for noticia in lista:
        if noticiaRemocao in noticia.titulo:
            encontrei = True
            lista.remove(noticia)    
            atualizarArquivo(lista)
            print('Notícia removida com sucesso!')

    if not encontrei:
        print("Notícia não encontrada!") 