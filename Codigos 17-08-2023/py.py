print("Sistema de triagem ambulatorial!")

nome=input("Informe o nome do paciente: ").upper()
idade=int(input("Informe a idade do paciente: "))

dor=int(input("Informe o nível de dor do paciente: "))

while(True):
    temperatura=float(input("Informe a temperatura do paciente: "))
    if (temperatura < 20 or temperatura > 60):
        print(f'A temperatura {temperatura} é inválida. Informe uma temperatura válida.')
    else:
        break
    

