x=10
y=5

#Podemos usar operadores de comparacion (==, !=, >, <, >=, <=)

#Simple if
if x>y:
	print('{0} es mas grande que {1}'.format(x,y))
else:
	print('{0} es mas grande que {1}'.format(y,x))

print('------')

if x>y:
	print('{0} es mas grande que {1}'.format(x,y))
elif x==y:
	print('{0} es igual  que {1}'.format(x,y))
else:
	print('{0} es mas grande que {1}'.format(y,x))

print('-------')

#if anidados

if x>2:
  if x<=10:
	print('{0} es mas grande que 2 e igual/menor a 10'.format(x))

print('-----------')

#una mejor forma de usarlos es con operadores logicos(and,or,not) se usan
#combinar

#and
if x>2 and x<=10:
	print('{0} es mas grande que 2 e igual/menor que 10'.format(x))

#or
if x>2 or x<=10:
	print('{0} es mas grande que 2 e igual/menor a 10'.format(x)) 

if not (x==y):
	print('{0} no  es igual a {1}'.format(x,y))



