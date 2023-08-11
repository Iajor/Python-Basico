#1 - Um usuário (diabético) de insulina rápida precisa fazer uso do medicamento sempre que for realizar
#    uma refeição. Assim, faça um programa que receba do usuário sua glicemia do momento (mg/dl),
#    meta pré-refeição (em geral é 100 mg/dl), fator de sensibilidade (valor inteiro entre 20 a 60). 
#    A partir desses valores, o programa deve calcular e exibir para o usuário a quantidade de insulina
#    que ele deverá administrar baseada na equação: 
#    quantidade_insulina = (glicemia_do_momento - meta_pre_refeicao) / fator_sensibilidade

print("Informe as seguintes informações ")
glicemiaMomento=int(input("Sua glicemia neste momento(mg/dl): "))
prerefeicao=int(input("Sua meta pré-refeição(mg/dl): "))
fatorSens=int(input("Seu fator de sensibilidade(entre 20 a 60): "))

qtdaInsulina=(glicemiaMomento-prerefeicao)/fatorSens

print(f'A sua quantidade necessária é {qtdaInsulina}')