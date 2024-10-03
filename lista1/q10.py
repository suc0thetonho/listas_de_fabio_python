n1 = float(input("Quanto de agua o primeiro competidor espirrou ?\n"
                 "Digite aqui: "))
n2 = float(input("Quanto de agua o segundo competidor espirrou ?\n"
                 "Digite aqui: "))
n3 = float(input("Quanto de agua o terceiro competidor espirrou ?\n"
                 "Digite aqui: "))

if (n1 < n2) and (n1 < n3):
    print("Quem ganhou foi o primeiro competidor!!")
elif (n2 < n1) and n2 < n3:
    print("Quem ganhou foi o segundo competidor!!")
elif(n3 < n1) and (n3 < n2):
    print("Quem ganhou foi o terceiro competidor")