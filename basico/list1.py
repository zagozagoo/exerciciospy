#Desenvolva um programa que armazene quatro notas em uma lista e que apresente: a média final, a maior nota e a menor nota
notas = []
contador = 1

while contador < 5:
    notas.append(float(input(f"insira respectivamente a {contador}a nota: ")))
    contador += 1

media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)

print(f"A media foi {media:.2f}, a menor nota foi {menor:.2f} e a maior foi {maior:.2f}")


