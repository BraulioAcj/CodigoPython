#abrir un archivo
miArchivo = open('miArchivo.txt','w')

#obtener info de este archivo
print('Name: ', miArchivo.name)
print('Esta cerrado: ', miArchivo.closed)
print('Modo abierto: ', miArchivo.mode)

#escribir algo al archivo
miArchivo.write('Me encanta Python')
miArchivo.write(' y ROOT')
miArchivo.close()

#leer un archivo
miArchivo = open ('miArchivo.txt','r+')
texto = miArchivo.read(20)
print(texto)
