for i in range (10):
    nome = input(f"DIGITE AQUI O NOME DA {i+1}: ")
    idade = int(input(F"DIGITE AQUI A IDADE DA{i+1}: "))
    sexo = int(input("DIGITE 1 SE A PESSOA É HOMEM\n"
                     "DIGITE 2 SE É MULHER\n"
                     "DIGITE AQUI: "))
    
    if (sexo == 1):
        if (idade > -1):
            homem_velho = nome
            idade_homem_velho = idade
    elif(sexo == 2):
        if idade < 121:
            mulher_mais_nova = nome
            idade_mulher_velha = idade

print(f"Nome do homem mais velho: {homem_velho}")
print(f"Nome da mulher mais nova: {mulher_mais_nova}")