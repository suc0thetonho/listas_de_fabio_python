valor = float(input("DIGITE AQUI A MASSA DO MATERIAL RADIOATIVO: "))
massa_i = valor
cont = 0
while(valor != 0):
    valor = valor/2
    cont+= 50
    if (valor < 0.5):
        break

horas = cont / 3600
minutos = (cont % 3600)/60
segundo = cont % 60

print(f"MASSA INICIAL: {massa_i}\nMASSA FINAL: {valor}")
print(f"TEMPO: {horas:.0f} : {minutos:.0f} : {segundo}")


