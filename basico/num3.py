#Desenvolva um programa que leia quatro notas e que apresente a média final
nota1 = float(input("Informe a nota da primeira prova: "))
nota2 = float(input("Informe a nota da segunda prova: "))
nota3 = float(input("Informe a nota da terceira prova: "))
nota4 = float(input("Informe a nota da quarta prova: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A media final eh: {media:.2f}")