
import random

cont = 0
cont2 = 0

caveira_invocada = random.randint(1000, 4000)
mago_negro = random.randint(1000, 4000)

dragao_azul = random.randint(1000, 4000)
genio = random.randint(1000, 4000)

print("PRIMEIRA BATALHA\n")
if (mago_negro > genio):
    print("VENCEDOR DA PRIMEIRA BATALHA: YUMI\n"
          "MAGO NEGRO VENCEU O DUELO\n")
    cont+=1
elif(genio > mago_negro):
    print("VENCEDOR DA 1 BATALHA: KAIBA\n"
          "GENIO VENCEU O DUELO\n")
    cont2+=1
print("SEGUNDA BATALHA\n")
if(caveira_invocada > dragao_azul):
     print("VENCEDOR DA 2 BATALHA: KAIBA\n"
           "SER ELETRICO DA ESCURIDÃO VENCEU O DUELO\n")
     cont2+=1
elif(dragao_azul > caveira_invocada):
    print("VENCEDOR DA 2 BATALHA: YUMI\n"
           "DRAGÃO BRANCO DOS OLHOS AZUIS VENCEU O DUELO\n")
    cont2+=1

if(cont2 == 2):
    print("KAIBA VENCEDOR DO DUELO")
elif(cont==2):
    print("YUMI VENCEDOR DO DUELO")
elif(cont == cont2):
    print("EMPATE")
