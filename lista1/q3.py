num = int(input("DIGITE AQUI UM NUMERO INTEIRO: "))

if (num%4==0) and (num%8==0):
    print(f"{num} é um numero multiplo de 4 e 8")
else:
    print(f"{num} não é um numero multiplo de 4 e 8")