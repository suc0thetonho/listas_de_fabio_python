print("========================================")
n1 = int(input("DIGITE 1 SE OS MONSTROS ERAM OS BONECOS DE MARSHMELLOW\n"
               "DIGITE 2 SE OS PROBLEMAS SÃO OS MORTOS\n"
               "DIGITE 3 SE OS PROBLEMAS SÃO VAMPITOS\n\n"
               "DIGITE AQUI: "))

n2 = int(input("DIGITE 1 SE OS MONSTROS ERAM OS BONECOS DE MARSHMELLOW\n"
               "DIGITE 2 SE OS PROBLEMAS SÃO OS MORTOS\n"
               "DIGITE 3 SE OS PROBLEMAS SÃO VAMPITOS\n\n"
               "DIGITE AQUI: "))

n3 = int(input("DIGITE 1 SE OS MONSTROS ERAM OS BONECOS DE MARSHMELLOW\n"
               "DIGITE 2 SE OS PROBLEMAS SÃO OS MORTOS\n"
               "DIGITE 3 SE OS PROBLEMAS SÃO VAMPITOS\n\n"
               "DIGITE AQUI: "))

n4 = int(input("DIGITE 1 SE OS MONSTROS ERAM OS BONECOS DE MARSHMELLOW\n"
               "DIGITE 2 SE OS PROBLEMAS SÃO OS MORTOS\n"
               "DIGITE 3 SE OS PROBLEMAS SÃO VAMPITOS\n\n"
               "DIGITE AQUI: "))
print("========================================")

if (n1 == 1):
    valor1 = 350
elif(n1 == 2):
    valor1 = 120
elif (n1 == 3):
    valor1 = 50

if (n2 == 1):
    valor2 = 350
elif(n2 == 2):
    valor2 = 120
elif (n2 == 3):
    valor2 = 50

if (n3 == 1):
    valor3 = 350
elif(n3 == 2):
    valor3 = 120
elif (n3 == 3):
    valor3 = 50

if (n4 == 1):
    valor4 = 350
elif(n4 == 2):
    valor4 = 120
elif (n4 == 3):
    valor4 = 50

print(f"TOTAL A SE PAGAR R$ {valor1+valor2+valor3+valor4}")