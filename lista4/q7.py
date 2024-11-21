import random
palpite = []

for i in range(6):
    numero = random.randint(1, 60)
    if (numero < 10):
        palpite.append("{:0>2}".format(numero))

    else:
        palpite.append(numero)

print("PALPITE DA MEGA SENA")

for numero in palpite:
    print(numero, end=" ")
