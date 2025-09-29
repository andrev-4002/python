#printar uma tupla
#crie uma tupla com alguns numeros inteiros e, em seguida, exiba o menor e o maior elemento.
#cie uma tupla com algumas palavras e exiba-as em ordem alfabética
#sorted
#tupla com os dias da semana e imprimir apenas os tres primeiros
#sum e len
#remove

numerosLoucosDemais = (2, 3, 7, 11, 5, 9)
minimo = min(numerosLoucosDemais)
maximo = max(numerosLoucosDemais)
print(numerosLoucosDemais)
print("O maior e o menor valor da tupla são, respectivamente:",minimo, "e,",maximo,'\n')

palavrasLegais = ("peixe", "caveira", "batuta", 'dinheiro', 'rock', 'supimpa', 'zambeta')
print("Organizando as palavras da tupla em ordem alfabética:", sorted(palavrasLegais),'\n')

diasDaSemana = ('domingo', 'segunada', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')
print("Os três primeiros dias da semana são:",diasDaSemana[:3],'\n')

numeros = [1, 5, 8, 12, 53]
print("soma dos números é:", sum(numeros))
print("a quantidade de números é:", len(numeros))
print("a média dos números é:", sum(numeros) / len(numeros))

print(numeros)
numeros.remove(12)
print(numeros)

#tuplas também servem para listas e dicionarios
roubo = ['um','sete','palavra','amogus','zarabitoinga','aaaaa']
print(sorted(roubo))
palavreadosFeios = {'bobão', 'feio', 'abestado', 'boboca', 'cabeça de mamão'}
print(sorted(palavreadosFeios))