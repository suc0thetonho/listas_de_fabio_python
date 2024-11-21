import random

homens_alto = []
homens_baixo = []

mulher_alta = []
mulher_baixa = []

for i in range(200):
    numero_homem = random.uniform(1.40, 2.36)
    homens_alto.append(numero_homem)
    homens_baixo.append(numero_homem)


for j in range(300):
    numero_mulher = random.uniform(1.35, 2.07)
    mulher_alta.append(numero_mulher)
    mulher_baixa.append(numero_mulher)

tamanho = len(homens_alto)
tamanho2 = len(mulher_alta)
troca = True
troca2 = True

while(troca == True and tamanho > 0):
    troca = False
    for j in range(tamanho-1):
        if (homens_alto[j] > homens_alto[j+1]):
            homens_alto[j], homens_alto[j + 1] = homens_alto[j + 1], homens_alto[j]

            homens_alto[j], homens_alto[j - 1] = homens_alto[j - 1], homens_alto[j]
            troca = True
        
    
    for j in range(tamanho-1):
        if (homens_baixo[j] < homens_baixo[j+1]):
            homens_baixo[j], homens_baixo[j + 1] = homens_baixo[j + 1], homens_baixo[j]

            homens_baixo[j], homens_baixo[j + 1] = homens_baixo[j + 1], homens_baixo[j]
            troca = True
    tamanho -= 1

while(troca2 == True and tamanho2 > 0):
    for j in range(tamanho2-1):
        if (mulher_alta[j] > mulher_alta[j+1]):
            mulher_alta[j], mulher_alta[j + 1] = mulher_alta[j + 1], mulher_alta[j]

            mulher_alta[j], mulher_alta[j - 1] = mulher_alta[j - 1], mulher_alta[j]
            troca2 = True

    for j in range(tamanho2-1):
        if (mulher_alta[j] < mulher_alta[j+1]):
            mulher_baixa[j], mulher_baixa[j + 1] = mulher_baixa[j + 1], mulher_baixa[j]

            mulher_baixa[j], mulher_baixa[j + 1] = mulher_baixa[j + 1], mulher_baixa[j]
            troca2 = True            
    tamanho2 -= 1


homem_maisbaixo = homens_alto[1]
homem_maisalto = homens_baixo[1]
mulher_maisbaixa = mulher_alta[1]
mulher_maisalta = mulher_baixa[1]


print(f"homem mais alto\n{homem_maisalto:.2f}\nhomem mais baixo\n{homem_maisbaixo:.2f}\nmulher mais alta\n{mulher_maisalta:.2f}\nmulher mais baixa\n{mulher_maisbaixa:.2f}")