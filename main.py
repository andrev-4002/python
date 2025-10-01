#1:--------------------------------------------------------------------------------
numeros = [12, 5, 8, 3, 10]
print("O resultado da soma dos números é: ", sum(numeros))


#2:--------------------------------------------------------------------------------
idadeParentes = [70, 45, 42, 15, 12]
print("O resultado da soma das idades dos parentes é: ", sum(idadeParentes))


#3:--------------------------------------------------------------------------------
n1 = input("Informe a nota N1 do aluno: ")
n2 = input("Informe a nota N2 do aluno: ")
n3 = input("Informe a nota N3 do aluno: ")
n4 = input("Informe a nota N4 do aluno: ")

media = (int(n1) + int(n2) + int(n3) + int(n4)) / 4

if media >= 7:
    print("Aluno está aprovado!\nNota: ", media)
else:
    print("Aluno está reprovado :(\nNota: ", media)


#4:--------------------------------------------------------------------------------
times = ("Vasco da Grama", "Flamingo", "Tira Água")
print(times[0], times[1], times[2])



#5:--------------------------------------------------------------------------------
print("ATENÇÃO PARA O TOQUE DE 5 X 2 SEGUNDOS!!!")

segundos = 10
while segundos > 0:
    print(segundos,"!!!")
    segundos -= 1
if segundos == 0:
    print("BRASIL-SIL-SIL-SIL")