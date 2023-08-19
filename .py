'''def soma(a,b):
    resultado = a + b
    return resultado
s = soma(1,2)
print(s)
'''

'''def dobrar_numero():
    numero = float(input("Digite um número:"))
    resultado = numero * 2
    return resultado
print('O dobro do número é: ', dobrar_numero())
'''
'''def soma_inteiros():
    numero1 = float(input("Digite o primeiro numero"))
    numero2 = float(input("Digite o segundo numero"))
    resultado = numero1 + numero2
    return resultado
print('O dobro do número é: ', soma_inteiros())
'''
'''def valor_absoluto():
    numero = float(input("Digite um número:"))
    resultado = abs(numero)
    return resultado
print('O modulo do numero é: ', valor_absoluto())
'''
'''def numero_quadrado():
    numero = float(input("Digite um numero"))
    resultado = numero**2
    return resultado
print('O valor do numero ao quadrado é: ', numero_quadrado())
'''
'''def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

n = int(input('Digite o numero que voce quer calcular o fatorial: '))
print('O fatorial de', n, 'é', fatorial(n))
'''

'''def maiornumero():
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    if numero1 > numero2:
        return numero1
    else:
        return numero2
print('O maior numero é: ', maiornumero())
'''

'''def antecessor():
    numero = float(input("Digite o numero: "))
    resultado = numero - 1
    return resultado
print('O antecessor do numero digitado é:, ', antecessor())
'''

def menornumero():
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    if numero1 < numero2:
        return numero1
    else:
        return numero2
print('O menor numero é: ', menornumero())
