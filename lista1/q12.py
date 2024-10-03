import random


profissao = random.randint(1,7)

caminho = int(input("DIGITE 1 PARA CAMINHO A\n"
                    "DIGITE 2 PARA CAMINHO B\n"
                    "DIGITE AQUI: "))

if(profissao == 1):
    salario = 50
    if(caminho == 1):
        salario = salario * 25
        print("MEDICO")
        print(f"PAGEMENTO TOTAL: R$ {salario}")
    elif(caminho == 2):
        salario = salario * (20+(5/2))
        print("MEDICO")
        print(f"PAGEMENTO TOTAL: R$ {salario}")

if(profissao == 2):
    salario = 24
    if(caminho == 1):
        salario = salario * 25
        print("JORNALISTA")
        print(f"PAGEMENTO TOTAL: R$ {salario}")
    elif(caminho == 2):
        salario = salario * (20+(5/2))
        print("JORNALISTA")
        print(f"PAGEMENTO TOTAL: R$ {salario}")


if(profissao == 3):
    salario = 50
    if(caminho == 1):
        salario = salario * 25
        print("ADVOGADO")
        print(f"PAGEMENTO TOTAL: R$ {salario}")
    elif(caminho == 2):
        salario = salario * (20+(5/2))
        print("ADVOGADO")
        print(f"PAGEMENTO TOTAL: R$ {salario}")


if(profissao == 4):
    salario = 24
    if(caminho == 1):
        print("PROFESSOR")
        salario = salario * 25
        print(f"PAGEMENTO TOTAL: R$ {salario}")
    elif(caminho == 2):
        salario = salario * (20+(5/2))
        print("PROFESSOR")
        print(f"PAGEMENTO TOTAL: R$ {salario}")


if(profissao == 5):
    salario = 30
    if(caminho == 1):
        salario = salario * 25
        print("FISICO")
        print(f"PAGEMENTO TOTAL: R$ {salario}")
    elif(caminho == 2):
        salario = salario * (20+(5/2))
        print("FISICO")
        print(f"PAGEMENTO TOTAL: R$ {salario}")


if(profissao == 6):
    salario = 12
    if(caminho == 1):
        salario = salario * 25
        print("COMERCIANTE")
        print(f"PAGEMENTO TOTAL: R$ {salario}")
    elif(caminho == 2):
        salario = salario * (20+(5/2))
        print("COMERCIANTE")
        print(f"PAGEMENTO TOTAL: R$ {salario}")


if(profissao == 7):
    salario = 16
    if(caminho == 1):
        salario = salario * 25
        print("ESTUDANTE")
        print(f"PAGEMENTO TOTAL: R$ {salario}")
    elif(caminho == 2):
        salario = salario * (20+(5/2))
        print("ESTUDANTE")
        print(f"PAGEMENTO TOTAL: R$ {salario}")
        