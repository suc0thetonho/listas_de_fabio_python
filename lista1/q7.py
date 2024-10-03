num1 = int(input("JOGADOR 1\nDIGITE 1 PARA PEDRA\nDIGITE 2 PARA PAPEL\nDIGITE 3 PARA TESOURA\nDIGITE AQUI: "))
print("===================================================")
num2 = int(input("JOGADOR 2\nDIGITE 1 PARA PEDRA\nDIGITE 2 PARA PAPEL\nDIGITE 3 PARA TESOURA\nDIGITE AQUI: "))

if (num1 == num2):
    print("DEU EMPATE")
else:
    #pedra papel
    if(num1 == 1) and (num2 == 2):
        print("JOGADOR 2 GANHOU")

    elif(num2 == 1) and (num1 == 2):
        print("JOGADOR 1 GANHOU")

    #papel tesoura

    elif(num1 == 2) and (num2 == 3):
        print("JOGADOR 2 GANHOU")

    elif(num1 == 3) and (num2 == 2):
        print("JOGADOR 1 GANHOU")
    

    #tesoura pedra

    elif(num1 == 3) and (num2 == 1):
        print("JOGADOR 2 GANHOU")
    
    elif(num2 == 3) and (num1 == 1):
        print("JOGADOR 1 GANHOU")

       
