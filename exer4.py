#4 - O volume de um cubo é determinado através do produto da área da base pela altura, 
#    (mas as arestas do cubo possuem medidas iguais), então temos que:
#    V = Ab * a ou V = a * a * a → V = a³. A partir disso, faça um programa, adequando as variáveis
#    para receber medidas de uma piscina (altura, largura e comprimento), para responder o volume de
#    água necessário para enchê-la.

altura=int(input("Informe a altura da piscina(m³): "))
largura=int(input("Informe a largura da piscina(m³): "))
comprimento=int(input("Informe o comprimento da piscina(m³): "))

print(f'O volume de água necessário para preencher a piscina é {altura*largura*comprimento:.0f} m³')


