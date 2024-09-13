import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# num01 = int(input("Insira um numero inteiro: "))
# num02 = int(input("Insira um numero inteiro: "))
# print(num01 + num02)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# num01 = int(input("Insira um numero inteiro: "))
# resto_divisao = num01 / 5
# print(resto_divisao)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# num01 = int(input("Insira um numero inteiro: "))
# num02 = int(input("Insira um numero inteiro: "))
# resultado = num01 * num02
# print(resultado)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

#numero_01 = int(input("Inserir um numero inteiro: "))
#numero_02 = int(input("Inserir um numero inteiro: "))
#resultado = numero_01 // numero_02
#print(resultado)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# num01 = int(input("Insira um numero inteiro: "))
# resultado = num01 ** 2
# print(resultado)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# num01 = float(input("Insira um numero flutuante: "))
# num02 = float(input("Insira um numero flutuante: "))
# print(num01 + num02)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# num01 = float(input("Insira um numero flutuante: "))
# num02 = float(input("Insira um numero flutuante: "))
# resultado = (num01+num02)/2
# print(resultado)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# num01 = float(input("Insira um numero flutuante: "))
# num02 = float(input("Insira um numero flutuante: "))
# resultado = num01 ** num02
# print(resultado)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# num01 = float(input("Insira temp em celcius: "))
# resultado = (num01*9/5)+32
# print(f"A temperura em Fahrenheit é: {resultado:.2f}")


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# raio_do_circulo = float(input("Digite o raio: "))
# area_do_circulo = math.pi * raio_do_circulo ** 2
# print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

#texto = input("Inserir um texto: ")
#texto_ajust = texto.upper()
#print(texto_ajust)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# texto = input("Insira nome completo do usuário: ")
# texto_min = texto.lower()
# print(texto_min)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# frase = input("Inserir uma frase: ")
# frase_ajust = frase.strip()
# print(frase_ajust)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data = input("Insira uma data no formato dd/mm/aaaa: ")
# lista_dia_mes_ano = data.split("/")
# print(f"O dia é: {lista_dia_mes_ano[0]}")
# print(f"O mês é: {lista_dia_mes_ano[1]}")
# print(f"O ano é: {lista_dia_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

#texto01 = input("Inseir um texto: ")
#texto02 = input("Inserir um texto: ")
#concat = texto01 + texto02
#print(concat)


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# x1 = False
# x2 = True
# resultado = x1 and x2
# print(f"O resultado do AND é: {resultado}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# x1 = False
# x2 = True
# resultado = x1 or x2
# print(f"O resultado do OR é: {resultado}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

#  = False
# resultado_not = not x1
# print(f"O resultado do NOT é: {resultado_not}")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# x1 = float(input("Inserir um número: "))
# x2 = float(input("Inserir um número: "))
# resultado = x1 == x2
# print(f"Os números são iguals? {resultado}")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# x1 = float(input("Inserir um número: "))
# x2 = float(input("Inserir um número: "))
# resultado = x1 != x2
# print(f"Os números são diferentes? {resultado}")

# #### try-except e if

# 21: Conversor de Temperatura

#try:
#    celsius = float(input("Digite a temperatura em Celsius: "))
#    fahrenheit = (celsius * 9/5) + 32
#    print(f"{celsius}°C é igual a {fahrenheit}°F.")
#except ValueError:
#    print("Por favor, digite um número válido para a temperatura.")

# 22: Verificador de Palíndromo

#texto = input("Inserir frase: ")

#if isinstance(texto, str):
#    texto_formatado = texto.replace(" ", "").lower()
#    if texto_formatado == texto_formatado[::-1]:
#        print("É um políndromo")
#    else:
#        print("Não é um políndromo")
#else:
#    print("Favor entrar com os dados corretos")

# 23: Calculadora Simples

# try:
#    metodo = input("Inserir o método + - x ou /: ")
#    num01 = float(input("Inserir um número: "))
#    num02 = float(input("Inserir um número: "))
#    if metodo == "+":
#        resultado = num01 + num02
#        print(resultado)
#    elif metodo == "-":
#         resultado = num01 - num02
#         print(resultado)
#    elif metodo == "x":
#         resultado = num01 * num02
#         print(resultado)
#    elif metodo == "/" and num02 != 0:
#         resultado = num01 / num02
#         print(resultado)
#    else:
#        print("Operador invalido ou divisão por 0")
#    
#except ValueError:
#    print("Favor inserir os dados corretos")

# 24: Classificador de Números

try:
    num = float(input("Inserir um número: "))
    if num < 0:
        print("Negativo")
    elif num > 0:
        print("Positivo")
    else:
        print("Zero")
    if num % 2 == 0:
        print("Par")
    else:
        print("ímpar")
except ValueError:
    print("Inserir dados corretos")
    
# 25: Conversão de Tipo com Validação
