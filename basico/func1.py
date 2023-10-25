#Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar
num = int(input("Insira um numero inteiro: "))
if num == 0:
    print("Insira numeros positivos e inteiros.")
elif num % 2 == 0:
    print(f"O numero {num} eh par.")
else:
    print(f"O numero {num} eh impar.")