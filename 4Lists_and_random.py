import random

# coin = random.randint(0, 1)

# if coin == 1:
#     print("Heads")
# else:
#     print("Tails")

# names_string = "Angela, Daniel, Victor, Breno, Caio, Vincius"
# names = names_string.split(", ") #Names agora eh uma lista, pois a funcao split tirou os "," e " " e transformou numa lista

# quantidade = random.randint(0, len(names) -1) #transforma a lista em numeros, e pega um desses numeros aleatoriamente
# aleatorio = names[quantidade] # com quantidade agora sendo numeros, e names a lista, aleatorio pega um valor de quantidade 
# print(len(names))             # e atribui esse valor o names_string correspondente em names.
# print(quantidade)
# print(aleatorio)

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter = position[0].lower()
print(letter)
"""
Na linha letter = position[0].lower(), o código está acessando o primeiro caractere da string position, que é a entrada do usuário para a posição desejada no mapa.

Quando o usuário insere a posição, ele fornece uma letra (representando a coluna) seguida por um número (representando a linha). Por exemplo, "A3". Portanto, position[0] se refere à primeira letra da entrada do usuário, que é a letra que representa a coluna no mapa.

Em Python, a indexação de strings e listas começa em 0, ou seja, o primeiro caractere ou elemento é acessado com o índice 0, o segundo com o índice 1, e assim por diante. Portanto, position[0] acessa o primeiro caractere da string position.
"""
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
print(letter_index)
number_index = int(position[1]) - 1
[print(number_index)]
map[number_index][letter_index] = "X"
"""
map: Aqui, map se refere à lista que contém o mapa. No código fornecido, map é uma lista que contém três listas, cada uma representando uma linha do mapa.

[number_index]: Isso está acessando a linha específica no mapa. Como number_index representa o índice da linha onde o usuário quer colocar o tesouro, esta parte acessa a linha correspondente na lista map. Por exemplo, se number_index for 2, isso acessará a terceira linha do mapa (lembrando que a indexação começa em 0).

[letter_index]: Depois de acessar a linha correta, isso acessa o elemento específico dentro dessa linha. Como letter_index representa o índice da coluna onde o usuário quer colocar o tesouro, esta parte acessa o elemento específico na linha selecionada. Por exemplo, se letter_index for 1, isso acessará o segundo elemento na linha selecionada.

Em resumo, map[number_index][letter_index] acessa a célula específica no mapa onde o usuário quer colocar o tesouro, com base nos índices fornecidos pelo usuário para a linha e coluna.
"""
print(map)





# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")