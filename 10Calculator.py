logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

"""
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
print(logo)
n1 = float(input("Qual é o primeiro número?: "))
print("+\n-\n*\n/\n")
type_of_operation = input("Escolha uma operação: ")
n2 = float(input("Qual é o próximo número?: "))
operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

result = operation[type_of_operation](n1, n2)
print("Resultado:", result)

keep = True
while keep:
    doing = input(f"Deseja continuar fazendo operações com {result}? Digite 'sim' para continuar ou 'nao' para finalizar. ")
    if doing.lower() == 'sim':
        type_of_operation = input("Escolha uma operação: ")
        n3 = float(input("Qual é o próximo número?: "))
        result = operation[type_of_operation](result, n3)
    elif doing.lower() == 'nao':
        keep = False
        print("Fim do programa")
    else:
        print("Opção inválida. Por favor, digite 'sim' para continuar ou 'nao' para finalizar!")
        