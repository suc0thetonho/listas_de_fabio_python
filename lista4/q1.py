import random

impar = []
par = []

for i in range(50):
    numero = random.randint(1,50)
    if(numero%2==0):
        par.append(numero)
    else:
        impar.append(numero)

print(f"PAR:\n{par}\nIMPAR:\n{impar}")