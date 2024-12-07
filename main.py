# MOSTRA NA TELA OS OPERADORES.
print('CALCULADORA')
print('Mostre os operadores de cálculos')
print('( + ) - adição')
print('( * ) - multiplicação')
print('( - ) - subtração')
print('( / ) - divisão')
print('Pressione qualquer outra tecla para sair')

# Inserir os valores para fazer os cálculos
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

# Seleciona o operador do cálculo
operador = input('Digite o operador de cálculo: ')

# Faz a validação do operador e realiza o cálculo
if operador not in ['+', '-', '*', '/']:
    print('OPERADOR INVÁLIDO, POR FAVOR COLOQUE UM OPERADOR CORRETO!!!')
else:
    if operador == '+':
        res = x + y
        print(f'A soma de {x} + {y} é igual a {res}')
    elif operador == '-':
        res = x - y
        print(f'A subtração de {x} - {y} é igual a {res}')
    elif operador == '/':
        res = x / y
        print(f'A divisão de {x} / {y} é igual a {res}')        
    elif operador == '*':
        res = x * y
        print(f'A multiplicação de {x} * {y} é igual a {res}')        
