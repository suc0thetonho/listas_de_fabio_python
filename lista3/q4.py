import random

num1 = random.randint(1,29)
num2 = random.randint(1,29)
num3 = random.randint(1,29)

if (num1 == num2) or (num1 == num3):
    num1 = random.randint(1,29)

elif (num2 == num1) or (num2 == num3):
    num2 = random.randint(1,29)

elif (num3 == num1) or (num3 == num2):
    num3 = random.randint(1,29)

print(f"{num1}\n{num2}\n{num3}")