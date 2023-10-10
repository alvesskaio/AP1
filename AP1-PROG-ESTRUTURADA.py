import sys # Utilizei o sys para encerrar o programa totalmente quando for aceita as condições
import random

def le_numero():
    while True: # O usuario ira definir o tamanho do dado, sendo 0 = tentar novamente, enter = sair
        texto = input('Informe um número: ')

        if texto == '':
            sys.exit()  #Atendendo ao proposto, ele encerrera todo o programa, interrompendo não apenas o loop, mas todo programa quando for uma string vazia.

        if texto.isnumeric():
            num = int(texto)
            if num > 0:
                return num
            
            print('O valor precisa ser maior que zero. ')
        else:
            print('A informação passada não é válida!')

def quantidade_de_dados(): # Aqui iremos coletar a quantidade de dados descrita pelo usuario.
    while True:
        quantidade = input('Digite o número de dados (em branco == 1): ')

        if quantidade == '':
            return 1
        else:
            if quantidade.isnumeric():
                quantidade = int(quantidade)
                if quantidade > 0:
                    return quantidade
                else:
                    print('A quantidade deve ser maior que zero.')
            else:
                print('Por favor, digite um número válido.')

def valores_random(lancamento, quantidade):  # Gerara os valores aleatorios de acordo com os tamanhos de dados e a quantidade de dados que foi preenchida pelo usuario
    resultados = []
    
    for _ in range(quantidade): # Utilizei o underscore devido aos ensinamentos na aula, que posso ditar qualquer nome e so ocupa espaço na memoria.
        resultado = random.randint(1, lancamento)
        resultados.append(resultado)
        
    return resultados

def imprimir_valores(valores):
    for valor in valores:
        print('Lançamento - ',valor)

numeros_de_lancamento = le_numero() # Agora pedimos o tamanho do dado

quantidade_dados = quantidade_de_dados() # O usuário irá definir quantos dados ele quer rodar

valores_aleatorios = valores_random(numeros_de_lancamento, quantidade_dados) # Gerar os valores aleatórios de acordo com a quantidade de dados desejados

imprimir_valores(valores_aleatorios) # Imprimira os valores aleatorios

print(f'{quantidade_dados} dado(s) de {numeros_de_lancamento} lados')
print(*valores_aleatorios, sep=' ')  # Vi que esse "*" faz com que ele saia da tupla, pois antes estava indo em formato de listas...