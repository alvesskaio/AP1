import random
import sys

while True: # O usuario ira definir o tamanho do dado, sendo 0 = tentar novamente, enter = sair
    tamanho_dos_dados = input('Forneça o tamanho do dado que será rolado (ENTER para sair): ')

    if tamanho_dos_dados == "":
        print('Programa encerrado..')
        sys.exit()

    try:
        tamanho_dos_dados = float(tamanho_dos_dados)
        if tamanho_dos_dados <= 0:
            print('O número deve ser maior que ZERO')
        else:
            break  # Para sair do loop caso essa condicao seja atendida
    except ValueError:
        print("Por favor, digite um número válido.")

def quantidade_de_dados(): # Aqui iremos coletar a quantidade de dados descrita pelo usuario.
    while True:
        quantidade = input('Digite o número de dados (em branco == 1): ')

        if quantidade == "":
            return 1
        else:
            try:
                quantidade = int(quantidade)
                if quantidade > 0:
                    return quantidade
                else:
                    print("A quantidade deve ser maior que zero.")
            except ValueError:
                print("Por favor, digite um número válido.")

def valores_random(tamanho_dos_dados, quantidade): # Gerara os valores aleatorios de acordo com os tamanhos de dados e a quantidade de dados que foi preenchida pelo usuario
    return [random.randint(1, tamanho_dos_dados) for _ in range(quantidade)]    # Utilizei o underscore devido aos ensinamentos na aula, que posso ditar qualquer nome e so ocupa espaço na memoria.

def imprimir_valores(valores):
    for i, valor in enumerate(valores, 1):
        print(f'Lançamento n{i} - {valor}')

quantidade_dados = quantidade_de_dados() # O usuario ira definir quantos dados ele quer rodar

valores_aleatorios = valores_random(tamanho_dos_dados, quantidade_dados) # Gerar os valores aleatorios de acordo com a quantidade de dados desejados


imprimir_valores(valores_aleatorios) # Imprimira os valores

print(f'\n{quantidade_dados} dado(s) de {tamanho_dos_dados} lados')
print(valores_aleatorios, sep=' ')