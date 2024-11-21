import random

cont = 0
cont2 = 0
cont3 = 0
cont4 = 0

cont_disparos_check = 0

nota = float(input("DIGITE AQUI A NOTA DA PROVA: "))

if (nota >= 7):
    cont += 1

sexo = int(input("DIGITE\n"
                      "1- SE VOCÊ SE CONSIDERA DO SEXO MASCULINO\n"
                      "2- SE VOCÊ SE CONSIDERA DO SEXO FEMININO\n"
                      "DIGITE AQUI: "))
corrida = float(input("DIGITE QUANTOS KM VOCÊ CORRIDA EM 2 KM: "))

if(sexo == 1):
    if (corrida >= 20):
        cont2+=1

elif(sexo == 2):
    if (corrida >= 10):
        cont2+=1

nadar = float(input("DIGITE QUANTOS KM VOCÊ NADOU EM 2 KM: "))

if(sexo == 1):
    if (nadar >= 10):
        cont3+=1

elif(sexo == 2):
    if (nadar >= 5):
        cont3+=1

for i in range(10):
    disparos = random.randint(1, 10)

    if(disparos%2 == 0):
        cont_disparos_check += 1

if(cont_disparos_check >= 6):
    cont4 += 1

print("")
if((cont != 1) or (cont2 != 1) or (cont3 != 1) or (cont4 != 1)):
    print("reprovado")
    if(cont!= 1):
        print("na etapa 1")
    elif(cont2!= 1):
        print("na etapa 2")
    elif(cont3!= 1):
        print("na etapa 3")
    elif(cont4!= 1):
        print("na etapa 4")
elif((cont and cont2 and cont3 and cont4) == 1):
    print("aprovado")