#3 - Refaça o programa anterior (refatorar) para que o programa recebe a distância e a velocidade média,
#    mas calcule e exiba o tempo da viagem.


distancia=int(input("Informe a distância a ser percorrida: "))
velMedia=int(input("Informe a velocidade média na qual deseja viajar: "))

print(f'A sua viagem levará {distancia/velMedia:.0f} horas')

