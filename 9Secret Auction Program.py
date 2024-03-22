logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)


def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record: # vou iterar dentro do dicionario bidding record
    bid_amount = bidding_record[bidder] # bid_amount = dentro do dicionario bidding_record(bids)[pego o valor associado a key do dicionario]
    if bid_amount > highest_bid: # aqui, ja com o valor que eu peguei do dicionario, verifico se eh maior que highest_bid
      highest_bid = bid_amount # vou usar essa variavel para testar nas proximas iteracoes se havera um bid maior que os valores anteriores
      winner = bidder # aqui, winner = bidder, que eh a key da variavel, definida na "funcao main" como nome
  print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {} # inicio um dicionario vazio
bidding_finished = False #deixo essa variavel falsa ppra iterar dentro do for

while not bidding_finished: # enquanto bidding_finished is true
  name = input("What is your name?: ") # pego o nome no input
  price = int(input("What is your bid?: $")) # pego o preco (bid) no input
  bids[name] = price #no dicionario bids, eu crio a key com a variavel name, e seu objeto no dicionario sera a variavel price.
  # print(bids) aqui, eu tenho um exemplo como: bids: {"daniel": 120, "lucas": 210,}
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True # caso a resposta for 'no', altera o valor da variavel e encerra o loop while.
    find_highest_bidder(bids)
  elif should_continue == "yes":
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")




