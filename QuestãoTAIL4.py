def identificar_estado(cpf) -> str:
    cpf_numeros = [int(digito) for digito in cpf if digito.isdigit()] #Aqui, confiro se os dados são todos números, como no código anterior

    if len(cpf_numeros) != 11: #Vejo se o tamanho está correto
        return False
    
    regiao_fiscal = cpf_numeros[8] #Como eu já sei a posição do digito verificador, que é o 9° digito, vou analisar apenas ele, então fixo a posição 8 da lista (já que python começa a contar do 0 e não 1)

    if regiao_fiscal == 1:
        return "DF, GO, MS, MT e TO"
    elif regiao_fiscal == 2:
        return "AC, AM, AP, PA, RO e RR"
    elif regiao_fiscal == 3:
        return "CE, MA, PI"
    elif regiao_fiscal == 4:
        return "AL, PB, PE, RN"
    elif regiao_fiscal == 5:
        return "BA e SE"
    elif regiao_fiscal == 6:
        return "MG"
    elif regiao_fiscal == 7:
        return "ES e RJ"
    elif regiao_fiscal == 8:
        return "PR e SC"
    elif regiao_fiscal ==0:
        return "RS"
  
"""
    Primeiro, chamo a função anterior para válidar o cpf antes de denotar a região fiscal, para não haver como burlar o sistema.
Então, apliquei if e elif's (else if) para denotar todas as regiões fiscais que o CPF apresenta, então se o dígito na posição
8 apresenta o dígito referente àquela região fiscal, os Estados dessa região são apresentados como strings pela função return.
"""   
    

