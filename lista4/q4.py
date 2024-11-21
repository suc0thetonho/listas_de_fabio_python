cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0
cont7 = 0
cont8 = 0
cont9 = 0
cont10 = 0
jogos = ["FATAL FURY: City of the Wolves",
          "Two Point Museum",
          "Indiana Jones e o Grande Círculo™",
          "Microsoft Flight Simulator 2024",
          "Wolfenstein: The Old Blood",
          "Minecraft",
          "Minecraft Dungeons",
          "Age of Mythology",
          "Forza Horizon 5",
          "Need for Speed™ Heat"]

for i in range(4):
    voto = int(input("1 - FATAL FURY: City of the Wolves\n"
          "2 - Two Point Museum\n"
          "3 - Indiana Jones e o Grande Círculo™\n"
          "4 - Microsoft Flight Simulator 2024\n"
          "5 - Wolfenstein: The Old Blood\n"
          "6 - Minecraft\n"
          "7 - Minecraft Dungeons\n"
          "8 - Age of Mythology\n"
          "9 - Forza Horizon 5\n"
          "10 - Need for Speed™ Heat\n"
          "DIGITE AQUI QUAL JOGO VOCE CONSIDERA POPULAR: "))

    if voto == 1:
        cont1 += 1
    elif voto == 2:
        cont2 += 1
    elif voto == 3:
        cont3 += 1
    elif voto == 4:
        cont4 += 1
    elif voto == 5:
        cont5 += 1
    elif voto == 6:
        cont6 += 1
    elif voto == 7:
        cont7 += 1
    elif voto == 8:
        cont8 += 1
    elif voto == 9:
        cont9 += 1
    elif voto == 10:
        cont10 += 1

quantidade = [cont1, cont2, cont3, cont4, cont5, cont6, cont7, cont8, cont9, cont10]

tamanho = len(quantidade)

troca = True

while(troca == True):
    troca = False
    for j in range(tamanho-1):
        if (quantidade[j] > quantidade[j+1]):
            quantidade[j], quantidade[j + 1] = quantidade[j + 1], quantidade[j]

            jogos[j], jogos[j + 1] = jogos[j + 1], jogos[j]
            troca = True
    tamanho -= 1

for k in range(len(jogos)):
    print(f"{k+1} colocado: {jogos[k]} : {quantidade[k]}\n")