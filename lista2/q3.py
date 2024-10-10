s = 0
sinal = 1

for i in range(50):
    num = (i + 1) * 2 * sinal
    s += num
    sinal *= -1

print(f'A soma dos 50 primeiro termos de S é {s}.')