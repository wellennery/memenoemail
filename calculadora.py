text = """
********** Python Calculator **********

Selecione o número da operação desejada:

1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
"""
print(text)

operacao = input ('Digita sua opção(1/2/3/4)')
y = int(input('Digite o primeiro número: '))
z = int(input('Digite o segundo número: '))

if operacao == "1":
    print("%s + %r = " %(y, z), y+z)
    
elif operacao == "2":
    print("%s - %r = " %(y, z),y-z)

elif operacao == "3":
    print("%s * %r = " %(y, z), y*z)

elif operacao == "4":
    print("%s / %r = " %(y, z),y/z)

else:
    print('Você está fazendo algo errado')


   