#7 - Faça um programa Python que receba duas notas, calcule a média aritmética e mostre o resultado.
#    Além disso, deve mostrar ao lado da média Aprovado (se média >= 7.0) Reprovado (se média <= 3.0),
#    Exame (se média entre 3.0 e 7.0)

nota1=int(input("Informe a nota 1:"))
nota2=int(input("Informe a nota 2:"))

media=(nota1+nota2)/2

if media >= 7:
    print('Aprovado!')
elif media <= 3:
    print('Reprovado!')
else:
    print("Está em exame!")