# Exemplo que causa TypeError

#try:
#    resultado = len(3)
#    print(resultado)
# except TypeError as e:   #tipos de erro possui uma doc de python sobre.
#    print(e)
# else:
#    print("Tudo ocorreu bem")
# finally:
#    print("O importante é participar.")


# numero = input("Insira um numero: ")
# if isinstance(numero, int):
#     print("A variável é um inteiro.")
# else:
#     print("A variável não é um inteiro.")


idade = 20
if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Exatamente 18 anos")
else:
    print("Maior de idade")