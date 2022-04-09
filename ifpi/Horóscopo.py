#Cria uma função chamada "signo" com dois com dois parâmetros "dia e mes", para infomar qual o signo do usuário.
def signo(dia, mes):
    if mes == 1:
        return 'Capricónio' if dia < 20 else 'Aquário'
    elif mes == 2:
        return 'Aquário' if dia < 19 else 'Peixes'
    elif mes == 3:
        return 'Peixes' if dia < 21 else 'Áries'
    elif mes == 4:
        return 'Áries' if dia < 20 else 'Touro'
    elif mes == 5:
        return 'Touro' if dia < 21 else 'Gêmeos'
    elif mes == 6:
        return 'Gêmeos' if dia < 22 else 'Câncer'
    elif mes == 7:
        return 'Câncer' if dia < 23 else 'Leão'
    elif mes == 8:
        return 'Leão' if dia < 23 else 'Virgem'
    elif mes == 9:
        return 'Virgem' if dia < 23 else 'Libra'
    elif mes == 10:
        return 'Libra' if dia < 23 else 'Escorpião'
    elif mes == 11:
        return 'Escorpião' if dia < 22 else 'Sargitário'
    elif mes == 12:
        return 'Sargitário' if dia < 22 else 'Capricórnio'

#Cria uma função intitulada "separar_data" com um parâmetro "dma", essa função serve para separa uma data em três variáveis.
def separar_data(dma):
    a = dma % 10000
    dma //= 10000

    m = dma % 100
    dma //= 100

    d = dma
    return d, m, a

#Cria uma função intitulada "remover_acentos" com o parâmetro "texto", essa função serve para formata uma stringer para uma url.
def remover_acentos(texto):
    from unicodedata import normalize
    
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

#Cria uma função chamada "horóscopo" com o parâmetro "signo_desejado". Ela serve para buscar o horóscopo do usuário, utilizando também as funções a cima.
def horoscopo(signo_desejado):
    import urllib.request

    signo_formatado = remover_acentos(signo_desejado).lower()
    
    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado
    
    requisicao = urllib.request.Request(
        url=minha_url,
        headers={'User-Agent':'Mozilla/5.0'}
    )
    
    resposta = urllib.request.urlopen(requisicao)
    pagina = resposta.read().decode('utf-8')

    marcador_inicio = '<p class="text-pred">'
    marcador_final = '</p>'

    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)
    final = pagina.find(marcador_final, inicio)

    return signo_desejado + ': ' + pagina[inicio:final]

# Cria uma função "main".
def main():
    #Entrada de dados.
    nascimento = int(input('Digite sua data de nascimento no formato DDMMAAAA: '))
    #Processamento
    dia, mes, _ = separar_data(nascimento)
    meu_signo = signo(dia, mes)
    horoscopo_de_hoje = horoscopo(meu_signo)
    #Saída de dados
    print(horoscopo_de_hoje)

#Uma condicionál para tornar o programa impotável e executável.
if __name__ == '__main__':
    main()