"""
    Implemente uma calculadora em Python, com instruções por linha de comando (CLI).
    A calculadora deve possuir as seguintes funcionalidades:

    Deve ficar em um loop infinito até o momento em que o usuário inserir um texto vazio (apertar ENTER); Feito

    Deve iniciar a calculadora no valor zero;


    Dentro do loop, executar as seguintes etapas:

    Ler um número; Feito
    Ler uma operação (soma, subtração, multiplicação ou divisão); Feito
    Ler outro número; Feito

    Exibir o resultado; Feito
    Pedir uma outra operação para continuar a conta ou “X” para limpar a calculadora;
    Se o usuário limpar a calculadora, ela deve recomeçar do zero.

    A calculadora deve exibir as informações na tela conforme o usuário for inserindo os dados.
    Assuma que o usuário passou apenas valores válidos (valores tipo float para os números,
    uma string vazia para sair do programa, uma das quatro operações básicas ou X para limpar
    a memória da calculadora).

"""
def leitura_dados(resultado_anterior=None):
    chama_op = True

    num1 = resultado_anterior
    if num1 is None:
        num1 = input("Informe um número, ou aperte ENTER para sair: ")

    operador = input("Operação (+, -, *, /), X para zerar ou ENTER para sair: ").lower()
    
    if operador == "x":
        resultado_anterior = None
        leitura_dados(resultado_anterior)

    num2 = input("Informe um número, ou aperte ENTER para sair: ")

    if num1 == "" or num2 == "":
        chama_op = False
    else:
        num1 = float(num1)
        num2 = float(num2)



    if chama_op:
        valida_dados(num1, operador, num2)


def valida_dados(num1, operador, num2):

        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            resultado = num1 / num2

        print(resultado)
        leitura_dados(resultado)

def main():
     leitura_dados()

main()





