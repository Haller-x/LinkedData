# -*- coding: latin-1 -*-

print("Seu primeiro código em python!\n\n")

#Isso é um comentário
'''
Isso também
'''

print('Em Python quase tudo é um objeto!\n\n')
#note que não há diferença entre aspas simples e duplas desde que sejam "pares"
print('Variáveis!\n')
print('''Imagine uma caixa, se você coloca um livro dentro da caixa, você deve lembrar que o livro está dentro da caixa,
se tirar o livro da caixa e colocar uma bola, você deverá lembrar que dentro da caixa há uma bola\n\n''')

print('TIPOS DE DADOS!\n')

print('String!')
dentro_da_caixa = 'livro'
print(dentro_da_caixa)
print(type(dentro_da_caixa))
print()#pula uma linha

dentro_da_caixa = 'bola'
print(dentro_da_caixa)

print('Int e Float')
num = 8
print(num, " Tipo:", type(num))
num_float = 8.5
print(num_float, " Tipo:", type(num_float))

print('Boleano!')
print(3 == 3)# Note que um '=' denota atribuição, enquanto dois '=' denotam comparação
print(num == num_float)
print('------')

print(bool(num))
print(bool(0))# (), [], {}, "", 0 e None retornam False!