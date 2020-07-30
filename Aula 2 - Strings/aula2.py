''' Strings'''

a = "   linked data    "
print(a.strip()) #remove qualquer espaço no começo ou no fim

a = "linked data"
print(a.lower()) #transforma tudo em lowercase

print(a.upper()) #transforma tudo em upper case

print(a.replace("linked","golden"))#altera as correspondências (linked) por golden

a = "linked-data"
print(a.split("-"))#Separa os itens da string usando o separador definido
print(a)
a = a.split('-')
print(a)

#Concatenando!
a = 'Linked'
b = ' Data'
c = a + b
print(c)

nome = 'Maria'
idade = 19
print('Ela se chama {} e tem {} anos'.format(nome,idade))

nome = 'Pedro'
idade = 22
print('Ele se chama {z} e tem {k} anos'.format(z=nome,k=idade))

num = '8'
repetir = 6
print(num * repetir)

print(int(num) * repetir)



numeros = '1234567890'
letras = 'abcde'
espaço = '      '
letras_numeros = ''

isalnum()	Returns True if all characters in the string are alphanumeric

isalpha()	Returns True if all characters in the string are in the alphabet

isdecimal()	Returns True if all characters in the string are decimals

isdigit()	Returns True if all characters in the string are digits

islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric


isspace()	Returns True if all characters in the string are whitespaces

isupper()	Returns True if all characters in the string are upper case

join()	Joins the elements of an iterable to the end of the string

count()	Returns the number of times a specified value occurs in a string


'''
Palavras reservadas (não podem ser usadas como variáveis)
    and	as	assert	break	class	continue
    def	del	elif	else	except	exec
    finally	for	from	global	if	import
    in	is	lambda	nonlocal	not	or
    pass	raise	return	try	while	with
    yield	True	False	None
'''
# Variáveis também não podem começar com números. Ex: 
    #3letras = 'abc'