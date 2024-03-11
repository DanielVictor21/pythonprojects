def busca_ordenada(lista, elemento) -> int:
  # Seu código aqui
    lista_ordenada = sorted(lista)  # Usei a função "sorted" para ordenar a lista de forma crescente, para fazer a busca ordenada à posteriori
    esquerda, direita = 0, len(lista_ordenada) - 1 # Com a lista ordenada, verifico a quantidade de elementos com a função len.
    """
        Aqui, denoto o começo da lista de esquerda (local 0), e o final da lista de direita (local -1).
    A esquerda seria definida como 0 em qualquer lista, pois o 1° elemento começa a ser contado na posição zero.
        Contudo, como eu quero que o código funcione em lista de qualquer tamanho, eu não posso definir um valor de uma lista arbitrária qualquer,
    e para isso utilizei o "-1", que é normalmente usado nesses casos.
    """
    while esquerda <= direita: #começo um loop para que seja possível verificar os elementos à esquerda, ou seja, no começo do código
        meio = (esquerda + direita) // 2 

        if lista_ordenada[meio] == elemento: 
            return meio
        elif lista_ordenada[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

"""
        Dentro do loop, o parâmetro principal é o cálculo do "meio", onde como esquerda e direita foram definidas anteriormente, vou calcular
    as posições dos elementos partindo do meio, podendo o elemento ser o próprio meio ou apenas "pulando casas" para direita ou esquerda a partir desse.
        Assim, caso o elemento não for o do meio, o loop while vai começar a calcular se o elemento está em um lugar "maior que o meio", pulando 1 posição
        a cada loop, até achar. Ou, de forma equivalente, caso o elemento não esteja numa posição maior que o meio, o loop vai começar a decrescer 1 posição
        ate encontrar o elemento. Caso o elemento for encontrado, retorna a sua posição, e caso não for, sai do loop e retorna -1.
    
"""


    
