print("TIPO DE PAGAMENTO")
print("===============================")
tipo = int(input("DIGITE 1 SE DESEJA PAGAR NO PIX\n"
                 "DIGITE 2 SE DESEJA PAGAR NO DINHEIRO\n"
                 "DIGITE 3 SE DESEJA PAGAR NO CARTÃO\n"
                 "DIGITE AQUI:"))
print("===============================")
n1 = float(input("Digite aqui o valor do pagamento: "))

if(tipo == 1):
    porcetagem = n1 *(11.11/100)
    total = n1 - porcetagem
    print(f"O preço final é R$ {total}")
elif(tipo == 2):
    print(f"O preço final é R$ {n1}")
elif(tipo == 3):
    print(f"O preço final é R$ {n1+3}")