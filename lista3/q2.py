soma = 0
sinal = -1

for i in range(100):
    num1 = (i+1) * 2 * sinal
    print(num1)
    num2 = (i+1) * 4
    print(num2)
    soma += num1/num2
    print(num1/num2)
    if ((i + 1) % 3 == 0):
        sinal = 1
    else:
        sinal = -1
print(f'A soma dos 100 primeiro termos de S é {soma}')