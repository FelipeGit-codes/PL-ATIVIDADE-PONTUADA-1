import os

os.system("cls")

valor_A = input("Digite o valor A: ")
Valor_B = input("Digite o valor B: ")
Valor_C = input("Digite o valor C: ")

soma = Valor_A + Valor_B

if soma <= Valor_C:
    print("A soma de A e B é menor que o valor C")
else:
    print("A soma é maior que valor C")