import random
cont = 0
for i in range(195):

    num = random.randint(12,299)
    if (num%11 == 0):
        cont +=1

print(f"FORAM ATINGIDOS {cont} PAISES  ")