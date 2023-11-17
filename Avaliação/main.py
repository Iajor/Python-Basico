#O programa final é um sistema de gestão de notícias. 

# A notícia deve ter título, categoria (esporte, política, entretenimento), texto (400 letras no máximo) e palavras-chave (3 obrigatoriamente).
# O sistema deve permitir que um usuário cadastre, altere, pesquise e remova uma notícia, que deve ser persistida em arquivo .csv (titulo;categoria;texto;palavras-chave).

# Para pesquisar, alterar ou remover uma notícia, deve haver um campo que o usuário o preencha. O sistema deve analisar título, categoria, texto e palavras-chave de todas as notícias cadastradas para efetuar a pesquisa, ou a alteração, ou remoção.

# Para ajudar:
# - criar classe Noticia (titulo, categoria, texto e palavras-chave)
# - usar lista
# - usar arquivo


import os
import metodos

listaNoticias = []

metodos.conexaoBase(listaNoticias)

while(True):
    os.system('cls')
    opcao=metodos.exibirMenu()

    if opcao == '1':
        metodos.cadastrarNoticia(listaNoticias)

    elif opcao == '2':
        metodos.alterarNoticia(listaNoticias)

    elif opcao == '3':
        metodos.pesquisarNoticia(listaNoticias)

    elif opcao == '4':
        metodos.removerNoticia()

    elif opcao == '5':
        print(listaNoticias)
        break

    else:
        print("Opcão inválida! Informe um opção válida.")
    
    os.system('pause')