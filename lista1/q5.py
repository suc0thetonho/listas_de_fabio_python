preco1  = 9
preco2 = 18
preco3 = 27
preco4 = 36
preco5 = 45
preco6 = 54
preco7 = 13
preco8 = 18
preco9 = 4.50 

print("TOTAL GASTO COM OS VALORES DO PEDÁGIO")
print("===============================")

num = int(input("DIGITE 1 SE VOCÊ VAI DE RECIFE/PE PARA CARUARU/PE\n"
                "DIGITE 2 SE VOCÊ VAI DE RECIFE/PE PARA ARCOVERDE/PE\n"
                "DIGITE 3 SE VOCÊ VAI DE RECIFE/PE PARA PETROLINA/PE\n"
                "DIGITE AQUI O NÚMERO: "))

print("===============================")


num2 = int(input("ESPECIFIQUE O TIPO DE VEÍCULO QUE VOCÊ OU O MOTORISTA VAI UTILIZAR\n"
                "DIGITE 1 PARA AUTOMÓVEL, CAMINHONETE, FURGÃO\n"
                "DIGITE 2 PARA CAMINHÃO LEVE, ÔNIBUS, CAMINHÃO E FURGÃO COM RODAGEM DUPLA\n"
                "DIGITE 3 PARA CAMINHÃO, CAMINHÃO C/ SEMIRREBOQUE E ÔNIBUS COM 3 EIXOS\n"
                "DIGITE 4 PARA CAMINHÃO C/ REBOQUE, CAMINHÃO C/ SEMIRREBOQUE COM 4 EIXOS\n"
                "DIGITE 5 PARA CAMINHÃO C/ REBOQUE, CAMINHÃO C/ SEMIRREBOQUE COM 5 EIXOS\n"
                "DIGITE 6 PARA CAMINHÃO C/ REBOQUE, CAMINHÃO C/ SEMIRREBOQUE COM 6 EIXOS\n"
                "DIGITE 7 PARA AUTOMÓVEL OU CAMINHONETE C/ SEMIRREBOQUE COM 3 EIXOS E RODAGEM SIMPLES\n"
                "DIGITE 8 PARA AUTOMÓVEL OU CAMINHONETE C/ REBOQUE COM 4 EIXOS E RODAGEM SIMPLES\n"
                "DIGITE 9 PARA MOTOCICLETA, MOTONETA E BICICLETA A MOTOR\n"
                "DIGITE AQUI: "))

# Cálculo do total de pedágio
total = 0

if num == 1:
    if num2 == 1:
        total = preco1
    elif num2 == 2:
        total = preco2
    elif num2 == 3:
        total = preco3
    elif num2 == 4:
        total = preco4
    elif num2 == 5:
        total = preco5
    elif num2 == 6:
        total = preco6
    elif num2 == 7:
        total = preco7
    elif num2 == 8:
        total = preco8
    elif num2 == 9:
        total = preco9

elif num == 2:  # Para Arcoverde, multiplicar por 2
    if num2 == 1:
        total = preco1 * 2
    elif num2 == 2:
        total = preco2 * 2
    elif num2 == 3:
        total = preco3 * 2
    elif num2 == 4:
        total = preco4 * 2
    elif num2 == 5:
        total = preco5 * 2
    elif num2 == 6:
        total = preco6 * 2
    elif num2 == 7:
        total = preco7 * 2
    elif num2 == 8:
        total = preco8 * 2
    elif num2 == 9:
        total = preco9 * 2
        
elif num == 3:  # Para Petrolina, multiplicar por 2
    if num2 == 1:
        total = preco1 * 2
    elif num2 == 2:
        total = preco2 * 2
    elif num2 == 3:
        total = preco3 * 2
    elif num2 == 4:
        total = preco4 * 2
    elif num2 == 5:
        total = preco5 * 2
    elif num2 == 6:
        total = preco6 * 2
    elif num2 == 7:
        total = preco7 * 2
    elif num2 == 8:
        total = preco8 * 2
    elif num2 == 9:
        total = preco9 * 2

print("")
print("=============")
print("VALOR PAGO:")
print(f"TOTAL A PAGAR: R$ {total:.2f}")



