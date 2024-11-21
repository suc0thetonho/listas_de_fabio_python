aprovados = []
nomes_aprovados = []
final = []
reprovado = []

for i in range(3):
    nome = input("DIGITE AQUI O SEU NOME: ")
    nota = float(input("DIGITE AQUI A NOTA: "))

    if(nota >= 6):
        aprovados.append(nota)
        nomes_aprovados.append(nome)
    elif(nota < 6)and(nota >= 4):
        final.append(nota)
    else:
        reprovado.append(nota)

tamanho = len(aprovados)
troca = True

while(troca):
    troca = False
    for j in range(tamanho-1):
        if (aprovados[j] < aprovados[j+1]):
            aprovados[j], aprovados[j + 1] = aprovados[j + 1], aprovados[j]

            nomes_aprovados[j], nomes_aprovados[j - 1] = nomes_aprovados[j - 1], nomes_aprovados[j]
            troca = True
    tamanho -= 1

print(f"QUANTIDADE DE ALUNOS NA FINAL: {len(final)}")
print(f"QUANTIDADE DE ALUNOS REPROVADOS: {len(reprovado)}")
print("\nAPROVADOS")

for k in range(len(aprovados)):
    print(f"{k+1} colocado: {nomes_aprovados[k]} : {aprovados[k]}\n")



