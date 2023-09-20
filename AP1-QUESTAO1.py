import random
import sys

while True: # usuario ira defini o tamanho do dado, sendo 0 = tentar novamente, enter = sair
    tamanho_dado = input('Forneça o tamanho do dado que será rolado (ENTER para sair): ')

    if tamanho_dado == "":
        print('Programa encerrado..')
        sys.exit()

    try:
        tamanho_dado = float(tamanho_dado)
        if tamanho_dado <= 0:
            print('O número deve ser maior que ZERO')
        else:
            break  # para sair do loop caso essa condicao seja atendida
    except ValueError:
        print("Por favor, digite um número válido.")

def quantidade_de_dados():
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

def gerar_valores(tamanho_dado, quantidade):
    return [random.randint(1, tamanho_dado) for _ in range(quantidade)]    

def imprimir_valores(valores):
    for i, valor in enumerate(valores, 1):
        print(f'Lançamento n{i} - {valor}')


quantidade_dados = quantidade_de_dados() # O usuario ira definir quantos dados ele quer rodar


valores_aleatorios = gerar_valores(tamanho_dado, quantidade_dados) # Gerar os valores aleatorios de acodro com a quantidade de dados desejados


imprimir_valores(valores_aleatorios) # Imprimira os valores

print(f'\n{quantidade_dados} dado(s) de {tamanho_dado} lados')