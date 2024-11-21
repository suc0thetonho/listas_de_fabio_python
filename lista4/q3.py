import random
par = 0
impar = 0

for i in range(1000):
    numero = random.randint(1, 1000)
    if (numero%2==0):
        par =+ numero
    else:
       impar =+ numero

print(f"RESULTADO DO SOMATORIO: {impar/par}")