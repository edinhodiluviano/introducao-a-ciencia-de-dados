def criar_lista_com_zeros(tamanho):
    lista = []
    n = 0
    while n < tamanho:
        lista.append(0)
        n = n + 1
    return lista


def criar_matriz_com_zeros(linhas, colunas):
    matriz = []
    n = 0
    while n < linhas:
        linha = criar_lista_com_zeros(colunas)
        matriz.append(linha)
        n = n + 1
    return matriz


def transpor(lista):
    linha = 0
    linhas = len(lista)
    coluna = 0
    colunas = len(lista[0])
    nova_lista = criar_matriz_com_zeros(colunas, linhas)
    while linha < linhas:
        while coluna < colunas:
            nova_lista[coluna][linha] = lista[linha][coluna]
            coluna = coluna + 1
        linha = linha + 1
        coluna = 0
    return nova_lista


def csv(nome_do_arquivo):
    f = open(nome_do_arquivo)
    lines = f.read().split()
    f.close()
    for n, line in enumerate(lines):
        lines[n] = line.split(',')
    dados = transpor(lines[1:])
    for n, linha in enumerate(dados):
        for i, valor in enumerate(linha):
            if '.' in dados[n][i]:
                dados[n][i] = float(dados[n][i])
            else:
                dados[n][i] = int(dados[n][i])
    return dados


def colunas(nome_do_arquivo):
    f = open(nome_do_arquivo)
    lines = f.read().split()
    f.close()
    colunas = lines[0]
    return colunas.split(',')
