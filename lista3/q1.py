import random

cont = 0

n1 = random.randint(1, 100)
n2 = random.randint(1, 100)
n3 = random.randint(1, 100)

num1 = None
num2 = None
num3 = None


while (n1 != num1) and (n2 != num2) and (n3 != num3):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    cont += 1

print(f"Foram necesaria {cont} tentativas para acertar as melodias")