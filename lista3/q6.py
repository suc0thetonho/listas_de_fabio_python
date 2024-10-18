import random


cont_v = 0


cont_loki = 0
cont_frandal = 0

cont_l = 0
cont_v = 0

cont_lo = 0
cont_si = 0
print("\nRESULTADOS")
print("===============================")

#loki x Voltstagg
loki_r = random.randint(1, 100)
volt = random.randint(1,100)

if(loki_r > volt):
    print("LOKI VENCEU VOLTSTAGG")
    cont_v += 1
else:
    print("LOKI PERDEU PRA VOLTSTAGG")

#Loki x Frandal
for i in range(10):

    loki_arco = random.randint(1, 60)
    if(loki_arco <= 50):
        cont_loki +=1
    else:
        cont_loki += 0

for j in range(10):

    frandal_arco = random.randint(1, 60)
    if(loki_arco <= 50):
        cont_frandal +=1
    else:
        cont_frandal += 0

if(cont_loki < cont_frandal):
    cont_v+=1
    print("LOKI VENCEU FRANDAL")
else:
    print("LOKI PERDEU PRA FRANDAL")

#Loki x Hogun

loki_d = random.randint(1, 5)
Hogun_d = random.randint(1, 5)

if(loki_d < Hogun_d):
    print("LOKI VENCEU HOGUN")
    cont_v+=1
else:
    print("LOKI PERDEU PRA HOGUN")

#Loki x Valquiria

while(True):
    loki = random.randint(1, 20)
    loki2 = random.randint(1, 20)

    valk = random.randint(1, 20)
    valk2 = random.randint(1, 20)

    if(loki == loki2):
        cont_l += 1
        break
    elif(valk == valk2):
        cont_v += 1
        break

if(cont_l > cont_v):
    print("LOKI GANHOU DE VALQUIRIA")
    cont_v += 1
else:
    print("LOKI PERDEU PRA VALQUIRIA")


#Loki x Lady Sif

for i in range(3):

    loki_ataque = random.randint(1,100)
    sif_ataque = random.randint(1, 100)

    loki_defesa = random.randint(1, 100)
    sif_defesa = random.randint(1, 100)

    if(loki_ataque%2 == 0) and (sif_defesa%2 != 0):
        cont_lo += 1
    elif(loki_defesa%2 != 0) and (sif_ataque%2 == 0):
        cont_si += 1

if(cont_lo > cont_si):
    print("LOKI GANHOU DE LADY SIF")
    cont_v += 1
else:
    print("LOKI PERDEU PRA LADY SIF")
print("===========================\n")


if(cont_v == 2):
    valor = int(input("DESEJA MANIPULAR UNS DOS RESULTADOS ?\n"
                      "DIGITE 1 PARA SIM\n"
                      "DIGITE 2 PARA NÃO\n"
                      "DIGITE AQUI: "))
    if(valor == 1):
        print("LOKI É O NOVO REI DE ASGARD")
elif(cont_v >= 3):
    print("LOKI É O NOVO REI DE ASGARD")

else:
    print("LOKI NÃO É O REI DE ASGARD")