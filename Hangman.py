import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words_list = ["musica", "saude", "computador", "livro", "salada"]

aleatorio = random.choice(words_list) # seleciono uma string aleatoria da lista

tamanho = len(aleatorio) # aqui, usando len, eu pego a quantidade de letras da palavra aleatoria selecionada
                         # se a palavra for saude, por exemplo, tamamho = 5

blank = [] # crio uma lista vazia
for letra in range(tamanho): # crio um for, para iterar do tamanho (usando range) da quantidade de letras de aleatorio, de 0 ate len -1.
    blank += "_" # para cada iteracao, eu troco o local de range por "_", entao de 0 a len -1, vou adicinar "_" na lista vazia

lives = 6
end_of_game = False #crio uma variavel bool, sendo falsa, para usar no while
print(f"Descubra a palavra! {blank}")
while not end_of_game: #como end_of_game original eh falsa, o while ira rodar ate que seja verdadeira (pq tem o not negando)
    guess = str(input("Descubre a palavra! digite 1 letra por vez: ")).lower() # pego a entrada do usuario, deixo para apenas ser string e uso lower() para todas serem iguais
    for position in range(tamanho): # aqui, a mesma coisa que o for passado, eu vou pegar a posicaoo (0, 1, 2, 3) de cada letra de tamanho = len(aleatorio)
        letter = aleatorio[position] # aqui, eu defino que a letra vai ser igual a posicao iterada no for. # por exemplo, se a palavra for salada, s = 0, a = 1, l = 2, e assim por diante
        if letter == guess: # caso a letra seja igual a do input, eu comparo com a lista "position", e coloco a letra no local da lista.
            blank[position] = letter
    if guess not in aleatorio:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lost!")
    if not "_" in blank:
        end_of_game = True
        print("You Won!")
    print(blank)
    print(stages[lives])
        


    


    


        
