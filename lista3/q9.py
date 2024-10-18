cont = 0 
cont2 = 0
cont3 = 0
cont4 = 0


valor = int(input("NUMERO DE CANAIS DISPONIVEIS\n"
                  "CANAL 4\n"
                  "CANAL 5\n"
                  "CANAL 7\n"
                  "CANAL 12\n"
                  "DIGITE AQUI O CANAL: "))

if (valor == 4):
    cont+=1
elif(valor == 5):
    cont2+=1
elif(valor == 7):
    cont3+=1
elif(valor == 12):
    cont4+=1

while(valor != 0):
    valor = int(input("NUMERO DOS CANAIS DISPONIVEIS\n"
                  "CANAL 4\n"
                  "CANAL 5\n"
                  "CANAL 7\n"
                  "CANAL 12\n"
                  "DIGITE AQUI O CANAL: "))

    if (valor == 4):
        cont+=1
    elif(valor == 5):
        cont2+=1
    elif(valor == 7):
        cont3+=1
    elif(valor == 12):
        cont4+=1


p1 = (cont/(cont+cont2+cont3+cont4))*100
p2 = (cont2/(cont+cont2+cont3+cont4))*100
p3 = (cont3/(cont+cont2+cont3+cont4))*100
p4 = (cont4/(cont+cont2+cont3+cont4))*100


print(f"PORCETAGEM DE AUDICENCIA\nCANAL 4: {p1} %\nCANAL 5: {p2}% \nCANAL 7: {p3}% \nCANAL 12: {p4}% ")