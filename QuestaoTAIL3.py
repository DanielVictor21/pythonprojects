def criptografar_cifra_vigenere(mensagem, chave) -> str:
  # Seu código aqui
    resultado = "" #Criei uma variável "resultado" para armazenar o resultado em uma string
    posição = 0 #crio posição = 0 para quando o loop começar, usá-la para ir somando a cada posição para conectar a letra, usando a função ord
    for letra in mensagem: #crio um loop for para letra iterar por cada caractere
        if letra.isalpha(): #aqui, com a estrutura condicional, verifico se a entrada do usuário foi uma letra do alfabeto, para poder dar continuade dentro da tabela fornecida acima
            deslocamento = ord(chave[posição % len(chave)]) - ord('A')
            resultado += chr((ord(letra) - ord('A') + deslocamento) % 26 + ord('A'))
            posição += 1
        else:
            resultado += letra
    return resultado

"""
    Agora, explicarei a partir de "deslocamento = ord(chave[posição % len(chave)]) - ord('A')"
 1°) Em chave[posição % len(chave)], eu acesso o caractere na posição 'posição' na chave, que no começo é 0, para ir adicionando aos poucos no loop.
 2°) Dentro do mesmo parâmetro, eu uso "%" para calcular o resto da chave, pois como nesse caso a chave "TAIL" não vai ser sempre do tamanho da mensagem a ser codificada,
 eu preciso garanti que quando acabarem as linhas eu possa voltar para o começo para ser cíclico. Exemplo: a chave "TAIL" tem 4 caracteres,
 mas se a posição for "21", fazendo 21 % 4 retorna 1, dai a 1° letra da chave vai ser acessada, gerando a ciclicidade.
 3°) uso ord() para obter o int (valor inteiro) que corresponde ao caractere da chave, para depois localizar na tabela.
 4°) dai, eu subtario ord('A'), pois usando o código ASCII, cada letra maiuscula seguida da outra tem diferença de 1 ponto, então com essa diferença, ord para a próxima letra.
    Assim, passando para "resultado += chr((ord(letra) - ord('A') + deslocamento) % 26 + ord('A'))", temos:
1°) ord(letra) eu uso para obter o valor inteiro da letra da mensagem.
2°) subtraio ord('A') aqui também para calcular a posição da letra em relação a A
3°) Daí, eu somo ao deslocamento que foi calculo anteriormente, para começar a aplicar a cifragem.
4°) Pego o resto por % 26 (letras do alfabeto) para garantir que permaneça dentro do intervalo das letras
5°) Por fim, adiciona-se ord('A') ao resultado para ajustar o valor para o intervalo de caracteres ASCII correspondente a letras maiúsculas.
 Isso é feito para garantir que o resultado seja um caractere ASCII válido, e no final, transformo esse caractere no char em letra correspondente usando chr()
    Finalizando, coloco "posição += 1" para avançar para a próxima letra da chave, e quando esse resultado for encontrado, adicioná-lo com letra e fazê-lo retornar.
 


"""