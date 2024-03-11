import re

"""
importei essa biblioteca para retirar caracteres alfanúmericos. Fiquei um tempo empacado nessa questão
por não saber como retirar a pontuação e o espaço, mas um amigo lembrou desse método e dai fui procurar como 
remover esses caracteres que teriam que ser ignorados, encontrando esse site: https://awari.com.br/python-remova-caracteres-de-uma-string
"""

def verificar_permuta(texto1, texto2) -> bool:
    texto1 = texto1.lower() #Transforma o texto1 em letras minúsculas, para não haver confusão de letra maiúscula ou minúscula
    texto2 = texto2.lower() #Transforma o texto2 em letras minúsculas, para não haver confusão de letra maiúscula ou minúscula

    pontuacao1 = re.sub('[^a-zA-Z0-9]', '', texto1) #peguei essa expressão do link citado acima, onde ele retirar caracteres não alfanuméricos.
    pontuacao2 = re.sub('[^a-zA-Z0-9]', '', texto2)

    caracteres_iguais1 = sorted(list(pontuacao1)) 
    caracteres_iguais2 = sorted(list(pontuacao2))
    """
        Aqui, eu havia transformado para lista apenas os algarismos alfanúmericos, pois por conta do método anterior, eu havia
    removido possíveis espaços e/ou pontuações. 
        Porém, quando fui testar na estrutura de repetição seguinte, não conseguia, pois no exemplo ('cat' e 'tAc', 
    o algoritmo tentava fazer 'cat' = 'tac') e fiquei empacado nisso, daí pedi ajuda ao chatgpt, que me recomendou a função "sorted"
    que organiza os caracteres em ordem alfabética. Assim, o exemplo ('cat' = 'tac') agora é lido como ('act' = 'act').
        Portanto, conseguia realmente ver se os caracteres eram iguais, pois estava na mesma ordem satisfazendo a igualdade.
    """

    return caracteres_iguais1 == caracteres_iguais2
    
"""
    Aqui, eu havia testado um if para retirar caso caracteres_iguais1 != caracteres_iguais2, um elif para comparar o tamanho
    (como está escrito acima) e um else para caso isso não fosse atendido. Porém, depois tentando otimizar percebi que usando apenas
    return caracteres_iguais1 == caracteres_iguais2 ja me retornava se fosse True o tamanho e os caracteres, além de caso não for,
    retornar false, encurtando o código
"""
