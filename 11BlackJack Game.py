import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""



def deal_card(): 
    """Retorna uma carta aleatoria do deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Calcula a soma das cartas, nesse caso, 2 cartas no comeco e mais caso precise posteriormente"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compare user vs computer score to see who wins!"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def playgame():
    print(logo)
    user_cards = [] # cria uma lista vazia para as cartas do usuario
    computer_cards = []# cria uma lista vazia para as cartas do computador
    is_game_over = False #cria uma variavel bool para usar em um loop proximo

    for _ in range(2): # fazendo essa iteracao, chama a funcao deal_card que retorna uma carta aleatoria, e repete isso 2 vezes.
        user_cards.append(deal_card()) # pega a lista vazia, e usa o append para colocar nela o retorno da funcao deal_card
        computer_cards.append(deal_card()) # pega a lista vazia, e usa o append para colocar nela o retorno da funcao deal_card

    while not is_game_over: # com o not, is_game_over = True, e assim vai rodar o jogo ate que alguma condicao torne a variavel False
        user_score = calculate_score(user_cards) # Retorna o calculo das 2 cartas do usuario. Tambem verificar se houve um blackjack ou Ace.
        computer_score = calculate_score(computer_cards) # Calculo do pc, tambem altera se Ace for 11 para 1, pois a carta tem essa propriedade.
        print(f" Your cards: {user_cards}, current score: {user_score}") # Mostra as 2 cartas do usuario e a sua soma
        print(f" Computer's first card: {computer_cards[0]}") # Mostra a primeira carta do computador

        if user_score == 0 or computer_score == 0 or user_score > 21: #caso haja blackjack, ou o usuario ultrapasse 21, acaba o jogo.
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ") #pede para o usuario escolher +1 carta 
        if user_should_deal == 'y':
            user_cards.append(deal_card()) # se a resposta = y, coloca +1 no deck do usuario, com a funcao append e a escolha aleatoria da funcao deal_card()
        else:
            is_game_over = True # Caso resposta = n, vai comparar os valores atuais.

    while computer_score !=0 and computer_score < 17: # verificar se o computador nao tem blackjack ou a soma < 17
        computer_cards.append(deal_card()) # caso nao, o computador pega mais 1 carta
        computer_score = calculate_score(computer_cards) # calcula o novo deck com a carta adicionada
    print(f" Your final hand: {user_cards}, final score: {user_score} ")
    print(f" Computer final hand: {computer_cards}, final score: {computer_score} ")
    print(compare(user_score, computer_score)) #usa a funcao compare(com varios if e elifs) para decidir quem ganhou o jogo.

while input(" DO you want to play a game of Blackjack? Type 'y' or 'n': ") == "y": #loop caso o player queira continuar jogando.
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    playgame()




