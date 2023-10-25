#Desenvolva um programa que armazene quatro notas em uma lista e que apresente a média final.
# Caso a média seja igual ou superior a 7, apresentar a mensagem "APROVADO", caso contrário,
# armazenar a nota da prova final e recalcular a média.
#Caso a nova média seja igual superior a 5, apresentar a mensagem "APROVADO", caso contrário, apresentar a mensagem "REPROVADO"
notas = []
contador = 1

while contador < 5:
    notas.append(float(input("Insira a nota da {contador}a prova: ")))
    contador += 1

media = sum(notas) / len(notas)
print(f"A media é: {media}")

if media >= 7:
    print("APROVADO!")
else:
    notas.append(int(input("Insira o valor da prova final: ")))

    media = sum(notas) / len(notas)
    print(f"A media atual é: {media}")

    if media >= 5:
        print("APROVADO")

    else:
        print("REPROVADO")
