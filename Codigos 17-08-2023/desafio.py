texto=input("Digite o texto: ").lower()
palavras=texto.split()
qtdPalavras=len(palavras)
artigos=[palavras[x] for x in range(len(palavras)) if palavras[x] == 'a' or palavras[x] == 'o'or palavras[x] =='as' or palavras[x] =='os' or palavras[x] == 'um' or palavras[x] == 'uma' or palavras[x] == 'uns' or palavras[x] == 'umas']

print("O texto foi dividido em uma lista que contém os seguintes elementros: ", palavras)
print(f'A quatidade de palavras é {qtdPalavras}')
print(f'A quatidade de artigos é {len(artigos)}')

