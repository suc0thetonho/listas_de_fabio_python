cont_onibus = 0
cont_carro = 0
cont_moto = 0

valor =int(input("DIGITE 1 PARA LIGAR O PROGRAMA\n"
                 "DIGITE 0 PARA DESLIGAR O PROGRAMA\n"
                 "DIGITE AQUI: "))

while(valor == 1):
    print("\n++++++++++++++++++++++")
    quanti = int(input("DIGITE 1 PARA ONIBUS\n"
                       "DIGITE 2 PARA CARRO\n"
                       "DIGITE 3 PARA MOTO\n"
                       "DIGITE AQUI: "))
    
    if(quanti == 1):
        cont_onibus += 1
    elif(quanti == 2):
        cont_carro += 1
    elif(quanti == 3):
        cont_moto +=1
    print("\n+++++++++++++++++++")
    valor =int(input("DIGITE 1 PARA CONTINUAR O PROGRAMA\n"
                 "DIGITE 0 PARA DESLIGAR O PROGRAMA\n"
                 "DIGITE AQUI: "))

print("\nLUCRO")
print("++++++++++++++")
print(f"R$: {(cont_onibus * 9)+(cont_carro*7)+(cont_moto*5.5)} de lucro")