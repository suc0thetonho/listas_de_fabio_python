import random

cont_italia = 0
cont_brasil = 0

num = random.randint(1,10)
num2 = random.randint(1,10)

num3 = random.randint(1,10)
num4 = random.randint(1,10)

num5 = random.randint(1,10)
num6 = random.randint(1,10)

num7 = random.randint(1,10)
num8 = random.randint(1,10)

num9 = random.randint(1,10)
num10 = random.randint(1,10)

if (num > num2):
    cont_italia+=1
elif (num2 > num):
    cont_brasil+=1

if (num3 > num4):
    cont_brasil+=1
elif (num4 > num3):
    cont_italia+=1

if (num5 > num6):
    cont_italia+=1
elif (num6 > num5):
    cont_brasil+=1

if (num7 > num8):
    cont_brasil+=1
elif (num8 > num7):
    cont_italia+=1

if (num9 > num10):
    cont_italia+=1
elif (num10 > num9):
    cont_brasil+=1

if(cont_italia > cont_brasil):
    print(f"ITALIA GANHOU A DISPUTA DE PENALTI POR {cont_italia} x {cont_brasil}")
elif(cont_brasil > cont_italia):
    print(f"BRASIL GANHOU A DISPUTA DE PENALTI POR {cont_brasil} x {cont_italia}")
else:
    print("SERA NECESSARIO UMA RODADA DE ALTERNANCIAS")