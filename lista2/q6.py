print("POTENCIA")
print("==============================================")
n1 = float(input("DIGITE O BASE: "))
n2 = int(input("DIGITE O EXPONENTE: "))

if (n2 > 0):
    for i in range(n2):
        resultado = n1*n1
elif (n2 < 0):
    n2 = n2*-1
    for i in range(n2):

        pot1 = n1*n1
    resultado = 1/pot1
else:
    print("RESULTADO\n"
          "1")

print("RESULTADO")
print(resultado)
