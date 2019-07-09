#UN FUNCION ES UN BLOQUE DE CODIGO QUE SOLO CORRE CUANDO SE LE LLAMA
#EN PYTHON NO USAMOS CORCHETES, USAMOS INDENTACION CON TABS O ESPACIO.

#Crear una funcion que solo imprime

def decirhola(nombre=''):
	print('Hola {0}'.format(nombre))
decirhola('Braulio y Paula')
decirhola()

#Funcion que nos regresa una variable
def suma(num1,num2):
	total= num1+num2
	return str(total)+' este numero es el resultado'
suma(2,3)
print(suma(2,3), type(suma(2,3)))

x=2
y=2
total= suma(x,y)
print(total, type(total))
print(total, type(total),"***lo mismo pero mas cool***")
