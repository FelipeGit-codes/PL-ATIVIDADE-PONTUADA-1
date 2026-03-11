import os 
os.system

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

print(f"A média entre {nota1} e {nota2} é: {media:.2f}")

if media >= 6.0:
    print("Aprovado")
elif media >= 4.0:
    print("Recuperação")
else:
    print("Reprovado")
