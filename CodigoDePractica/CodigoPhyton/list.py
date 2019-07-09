num = [1,2,3,4,5]
fruits = ['Manzanas','Naranjas','Uvas','Peras']

#Crear una lista, usando constructor
num2 = list((1,2,3,4,5))
print(num,fruits)

#Obtener un valor de la lista
print(fruits[3])

#Obtener magnitud
print(len(fruits))

#Agregar a la lista
fruits.append('Tunas')
print(fruits)

#Remover de la lista
fruits.remove('Uvas')
print(fruits)

#insertar en una posicion
fruits.insert(2,'Frambuesa')
print(fruits)

#Remover de una posicion con pop
fruits.pop(2)
print(fruits)

#Invertir la lista
fruits.reverse()
print(fruits)

#Acomodar alfabeticamente
fruits.sort()
print(fruits)
