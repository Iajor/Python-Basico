#6 - Construa um programa em Python em que o usuário insira a sigla de um estado brasileiro em que 
#    uma pessoa nasceu e, em seguida imprima uma das seguintes mensagens: 
#    Carioca Paulista Mineiro Outros estados

estados={
    'RJ': 'carioca',
    'SP': 'paulista',
    'MG': 'mineiro'
}

sigla=(input("Informe a sigla: ")).upper()


print(f'A sigla representa {estados.get(sigla, "outros estados")}')