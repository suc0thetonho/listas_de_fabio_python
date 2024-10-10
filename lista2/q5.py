import random
num_winner = 0
nome = None

jesse = random.randint(1,100)
barry = random.randint(1,100)
max = random.randint(1,100)
wells = random.randint(1,100)
jay = random.randint(1,100)
wally = random.randint(1,100)
print("+++++++++++++++++++++++++++++++++++")
print("velocidade de cada um")
print(f"jesse quick: {jesse*300000} km/s")
print(f"barry allen: {barry*300000} km/s")
print(f"max marcury: {max*300000} km/s")
print(f"dr wells: {wells*300000} km/s")
print(f"jay garrick: {jay*300000} km/s")
print(f"wally west: {wally*300000} km/s")

if (jesse > num_winner):
    num_winner = jesse
    nome = "jesse quick"

if (barry > num_winner):
    num_winner = barry
    nome = "barry allen"

if (max > num_winner):
    num_winner = max
    nome = "max marcury"

if (wells > num_winner):
    num_winner = wells
    nome = "dr wells"

if (jay > num_winner):
    num_winner = jay
    nome = "jay garrick"

if(wally > num_winner):
    num_winner = wally
    nome = "wally west"

print("")
print("===========VENCEDOR===========")
print(f"O vencedor foi {nome} com os seus: {num_winner*300000}")

