import random

cont = 0

for i in range(150):
    n1 = random.randint(1,2)

    if(n1 == 1):
        cont+=1

print(f"TOTAL DE QUEIJO: {cont}")