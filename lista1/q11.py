tempo = 0
print("=======================================================")
n1 = int(input("DIGITE 1 SE CHICO BENTO VAI A PÉ\n"
               "DIGITE 2 SE CHICO BENTO VAI DE BOTINA\n"
               "DIGITE 3 SE ELE VAI MONTADO NO TEOBALDO\n"
               "DIGITE AQUI: "))
print("")
print("=======================================================")
n2 = int(input("DIGITE 1 SE PARA NO RIACHO\n"
               "DIGITE 2 SE ELE ENTRA NO POMAR DE NHÔ LAU\n"
               "DIGITE 3 SE ELE TROCA PTILINA COM ROSINHA\n"
               "DIGITE 4 SE ELE FOI SURPREENDIDO POR UMA ONÇA\n"
               "DIGITE 5 SE NÃO HOUVE ALGUMA INTERFERENCIA\n"
               "DIGITE AQUI: "))
print("=======================================================")
print("")
if(n1==1):
    tempo = 50
    if(n2 == 1 ):
        tempo = tempo+40
    elif(n2 == 2 ):
        tempo = tempo + 20
    elif(n2 == 3):
        tempo = tempo+10
    elif(n2 == 4):
        tempo = 30

elif(n1==2):
    tempo = 40
    if(n2 == 1 ):
        tempo = tempo+40
    elif(n2 == 2 ):
        tempo = tempo + 20
    elif(n2 == 3): 
        tempo = tempo+10
    elif(n2 == 4):
        tempo = 30
    

elif(n1==3):
    tempo = 30
    if(n2 == 1 ):
        tempo = tempo+40
    elif(n2 == 2 ):
        tempo = tempo + 20
    elif(n2 == 3):
        tempo = tempo+10
    elif(n2 == 4):
        tempo = 30
    
if (tempo >= 60):
    print(f"ELE LEVOU {tempo/60} horas")
else:
    print(F"ELE LEVOU {tempo} minutos")