#2 - Faça um programa que ajude motoristas calcular e estimar viagens com diferentes tempos de viagem.
#    O programa deve receber do usuário do sistema (motorista) a distância a ser percorrida e o tempo
#    desejado da viagem. A partir disso, o programa deve calcular e exibir na tela a velocidade média
#    necessária.

distancia=int(input("Informe a distância a ser percorrida: "))
tempoDesejado=int(input("Informe o tempo que deseja levar: "))

print(f'A sua velocidade média deve ser {distancia/tempoDesejado:.0f} km/h')

