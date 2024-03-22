numeros = []

numero = int(input("Digite um número: "))

while numero != 1 and numero != 0:
    r = numero % 2
    numeros.append(str(r))  # Convertendo o resultado para string antes de adicionar à lista
    numero = numero // 2

# Converter a lista em uma lista reversa e, em seguida, em uma string
lista_reversa = list(reversed(numeros))
lista_string = ''.join(lista_reversa)

print(lista_string)