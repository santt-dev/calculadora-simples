""" import requests
from tkinter import *


"""
def calcular(operador, num1, num2):
    try:
        if operador == '+':
            return num1 + num2
        elif operador == '-':
            return num1 - num2
        elif operador == '*':
            return num1 * num2
        elif operador == '/':
            return num1 / num2
        else:
            raise ValueError("Operador inválido.")
    except ZeroDivisionError:
        print("Divisão por zero não é permitida.")
        return None
    except ValueError:
        print("Entrada inválida. Por favor, digite números.")
        return None


def main():
    while True:
        print('CALCULADORA')
        num1 = float(input('Digite o primeiro número: '))
        operador = input("Digite o operador (+, -, *, /): ")
        num2 = float(input('Digite o segundo número: '))
        resultado = calcular(operador, num1, num2)
        if resultado is not None:
            print("Resultado:", resultado)
        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != 's':
            break

main()

"""
janela = Tk()


janela.mainloop()

"""
