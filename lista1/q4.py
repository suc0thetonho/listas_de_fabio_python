print("PASTEL DO HOMER")
num1 = int(input("DIGITE 1 SE SERA UM PASTEL DE CARNE\n"
                 "DIGITE 2 SE SERA UM PASTEL DE FRANGO\n"
                 "DIGITE 3 SE SERA UM PASTEL DE QUEIJO\n"
                 "DIGITE AQUI: "))

print("PASTEL DO MARGE")
num2 = int(input("DIGITE 1 SE SERA UM PASTEL DE CARNE\n"
                 "DIGITE 2 SE SERA UM PASTEL DE FRANGO\n"
                 "DIGITE 3 SE SERA UM PASTEL DE QUEIJO\n"
                 "DIGITE AQUI: "))

print("PASTEL DO LISA")
num3 = int(input("DIGITE 1 SE SERA UM PASTEL DE CARNE\n"
                 "DIGITE 2 SE SERA UM PASTEL DE FRANGO\n"
                 "DIGITE 3 SE SERA UM PASTEL DE QUEIJO\n"
                 "DIGITE AQUI: "))

print("PASTEL DO MAGGIE")
num4 = int(input("DIGITE 1 SE SERA UM PASTEL DE CARNE\n"
                 "DIGITE 2 SE SERA UM PASTEL DE FRANGO\n"
                 "DIGITE 3 SE SERA UM PASTEL DE QUEIJO\n"
                 "DIGITE AQUI: "))

print("PASTEL DO BART")
num5 = int(input("DIGITE 1 SE SERA UM PASTEL DE CARNE\n"
                 "DIGITE 2 SE SERA UM PASTEL DE FRANGO\n"
                 "DIGITE 3 SE SERA UM PASTEL DE QUEIJO\n"
                 "DIGITE AQUI: "))

#pastel do homer
if (num1 == 1):
    preco1 = 12.5
elif(num1 == 2):
    preco1 = 11.11
elif (num1 == 3):
    preco1 = 10

#pastel da marge
if (num2 == 1):
    preco2 = 12.5
elif(num2 == 2):
    preco2 = 11.11
elif (num2 == 3):
    preco2 = 10

#pastel da lisa
if (num3 == 1):
    preco3 = 12.5
elif(num3 == 2):
    preco3 = 11.11
elif (num3 == 3):
    preco3 = 10

#pastel da maggie
if (num4 == 1):
    preco4 = 12.5
elif(num4 == 2):
    preco4 = 11.11
elif (num4 == 3):
    preco4 = 10

#pastel da marge
if (num5 == 1):
    preco5 = 12.5
elif(num5 == 2):
    preco5 = 11.11
elif (num5 == 3):
    preco5 = 10


print(f"O TOTAL DO PREÇO FOI: R$ {preco1+preco2+preco3+preco4+preco5:.2f}")