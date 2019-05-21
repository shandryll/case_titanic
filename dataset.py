import re

# Guardar em uma variável a abertura do CSV em modo de leitura
titanic_csv = open('titanic.csv', 'r')

# Ler o CSV identificando cada linha, e jogar o conteúdo lido em uma variável
linhas = titanic_csv.readlines()

# Posicionar o cursor no inicio do CSV para que quando for ler novamente, não aconteça um erro
titanic_csv.seek(0)

# Como os dados estão na varíável alocada, devemos fechar a leitura do arquivo para que possamos ter mais memória
titanic_csv.close()

# Separar os dados do cabeçalho e colocá-los em uma variável
headers = linhas[0].split(',')

# Criar uma variável que receberá os dados contidos na linha 1, separados por virgula
dados = linhas[1].split(',')

# Função criada para alterar a ordem que o nome vem, ignorando totalmente a vírgula
def tratar_nome(linha):
    match = re.compile(r'"(.*)(,)(\s.*)"')
    return match.sub(r'"\3 \1"', linha)

linha1_tratada = tratar_nome(linhas[1])
linha1_separada = linha1_tratada.split(',')

# Criação do dicionário vazio
titanic_data = {}

# Adiciona a cada item do cabeçalho uma lista vazia para receber o restante dos dados
for coluna in headers:
    titanic_data[coluna] = []

dados_tratados = []

# Inserindo em cada lista os dados ignorando o cabeçalho, pegando cada linha tratada e dando split
for dado in linhas[1:]:
    dado_tratado = tratar_nome(dado)
    dado_como_lista = dado_tratado.split(',')
    # Criar uma lista para receber os dados convertidos, colocando-os nas listas aninhadas
    dados_tratados.append(dado_como_lista)

'''
# Pegando o indice para correlacionar com as colunas existentes
for passageiro in dados_tratados:
    print(passageiro)
    for indice, dado in enumerate(passageiro):
        print("Índice:", indice, "Dado:", dado)
'''

# 1 - Pegar cada linha da varíavel dados_tratados e colocar em passageiro
# 2 - Fazer um for em passageiro e pegar o indice junto com os outros dados
# 3 - Ir na variavel coluna e pegar a coluna no seu respectivo indice
for passageiro in dados_tratados:
    for indice, dado in enumerate(passageiro):
        coluna = headers[indice]
        titanic_data[coluna].append(dado)

# Converter os dados vazios que vieram do campo de Age
for indice, age in enumerate(titanic_data['Age']):
    if titanic_data['Age'][indice] != '':
        titanic_data['Age'][indice] = float(age)
    else:
        titanic_data['Age'][indice] = 0

print(titanic_data)