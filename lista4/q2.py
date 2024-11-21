
mulheres = []
troca = True
for i in range(3):
    nome = input("DIGITE AQUI DA PESSOA: ")
    sexo = int(input("DIGITE 1 SE A PESSOA É DO SEXO FEMININO\n"
                     "DIGITE 2 SE O SEXO DA PESSOA É MASCULINO\n"
                     "DIGITE AQUI: "))
    if (sexo == 1):
        mulheres.append(nome)


tamanho_mulheres = len(mulheres)
while (troca == True):
    troca = False
    for j in range(tamanho_mulheres-1):
        if (mulheres[j] > mulheres[j+1]):
            mulheres[j], mulheres[j + 1] = mulheres[j + 1], mulheres[j]
            troca = True
    tamanho_mulheres -= 1

print(mulheres)
