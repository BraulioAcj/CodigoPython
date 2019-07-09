#Hola mundo, mi primer programa

print('Hola mundo')

x = 1              #int
y = 2.5            #float
name = 'jhkljglj'     #Str
is_cool = True     #bool 

#Otra forma de escribirlo (Multiple definicion)...
x, y, name, is_cool = (1,2.5,'Paula',True)

#matematicas basicas
a=x+y
print(a,x,y,name,is_cool)

#Checar el tipo de x
print(type(x))

#Redefinir
x = str(x)	#passing x
y = int(y)	#passing y
z = float(y)	

print(type(y),y)
print(type(z),z)
