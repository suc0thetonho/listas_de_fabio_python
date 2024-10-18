

idade_novo = 100

segunda_mulher_mais_velha_nome = ""
segunda_mulher_mais_velha_idade = 0

maior_idade_mulher_nome = ""
maior_idade_mulher_idade = 0

cont = 0
cont2 = 0

valor = int(input("DIGITE 1 PARA INICIALIZAR\n"
                  "DIGITE 0 PARA DESLIGAR O CÓDIGO\n"
                  "DIGITE AQUI: "))
print("")
if (valor != 1) and (valor != 0):
    print("")
    print("NUMERO INVALIDO\n")
    valor = int(input("DIGITE 1 PARA INICIALIZAR\n"
                      "DIGITE 0 PARA DESLIGAR O CÓDIGO\n"
                      "DIGITE AQUI: "))
while (valor == 1):
    print("===========================")
    nome = input("DIGITE AQUI O SEU NOME: ")
    idade = int(input("DIGITE AQUI A SUA IDADE: "))
    sexo = int(input("DIGITE 1 PARA SEXO MASCULINO\n"
               "DIGITE 2 PARA SEXO FEMININO\n"
                     "DIGITE AQUI O SEXO: "))
    
    print("")
    print("=====================")
    valor = int(input("DIGITE 1 PARA CONTINUAR\n"
                      "DIGITE 0 PARA DESLIGAR O CÓDIGO\n"
                      "DIGITE AQUI: "))
    print("")
    
    if ((sexo == 1) and (idade >= 18) and (idade < idade_novo)):
            idade_novo = idade
            cont+=1

    elif (sexo == 2):

        if (idade > maior_idade_mulher_idade):

            segunda_mulher_mais_velha_nome = maior_idade_mulher_nome
            segunda_mulher_mais_velha_idade = maior_idade_mulher_idade
            
            maior_idade_mulher_nome = nome 
            maior_idade_mulher_idade = idade

            cont2 += 1
        elif (idade > segunda_mulher_mais_velha_idade):

            segunda_mulher_mais_velha_nome = nome
            segunda_mulher_mais_velha_idade = idade
            cont2 += 1


if(cont > 0)and(cont2 > 0):
    print("\n=======================")
    print(f"IDADE DO HOMEM MAIS NOVO SENDO DE MAIOR: {idade_novo}")
    print(f"NOME DA SEGUNDA MULHER MAIS VELHA: {segunda_mulher_mais_velha_nome}")

elif(cont > 0)and(cont2 == 0 ):
    print("\n=======================")
    print(f"IDADE DO HOMEM MAIS NOVO SENDO DE MAIOR: {idade_novo}")
    print("NÃO HÁ UMA SEGUNDA MULHER MAIS VELHA")

elif(cont2 > 0) and (cont == 0):
     print("\n=======================")
     print(f"NÃO HÁ UM HOMEM MAIS NOVO ENTRES OS MAIORES DE IDADE")
     print(f"NOME DA SEGUNDA MULHER MAIS VELHA: {segunda_mulher_mais_velha_nome}")

else:
    print("\n=======================")
    print(f"NÃO HÁ UM HOMEM MAIS NOVO ENTRES OS MAIORES DE IDADE")
    print("NÃO HÁ UMA SEGUNDA MULHER MAIS VELHA")
