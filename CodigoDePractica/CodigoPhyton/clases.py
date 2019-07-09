#Una clase es como un nplano para crear un objeto. Un objeto es una instancia
#dentro de una clase que contine atributos y metodos.

#Crear una clase
class Usuario:
     #Constructor (funcion que corre cuando haces una instanciacion)
     def __init__(self, nombre, email, edad):
         self.nombre = nombre
         self.email = email	
	 self.edad = edad
 
     def saludos(self,num1=1):
	 print(num1)
         return 'Me llamo {0} y tengo {1}'.format(self.nombre,self.edad)

     def tengo_cumple(self):
         self.edad+=1

#Init un objeto para el usuario
Paula=Usuario('Paula', 'pau8a16gmail.com', 18)
print(type(Paula))
print(Paula.nombre)
print(Paula.saludos('Hola'))

#Extender la clase usuario
class Cliente(Usuario):
	#Constructor (funcion que corre cuando haces una instanciacion de una clase)
     def __init__(self,nombre,email,edad):
	  self.nombre = nombre
	  self.email = email
          self.edad = edad
	  self.saldo = 0
	
     def establecer_saldo(self,saldo):
	  self.saldo = saldo

     def saludos(self):
          return 'Me llamo {0}, tengo {1} y mi saldo es {2}'.format(self.nombre,self.edad,self.saldo)
		
#Init un cliente
Paula = Usuario('Paula Ochoa','pau8a16@gmail.com',18)
print(type(Paula))
print(Paula.nombre)
print(Paula.saludos('d'))

Paula.tengo_cumple
print(Paula.saludos)
print('--------------------')

#Init un cliente
Paula_usuario = Usuario('Paula Ochoa', 'pau8a16@gmail.com', 2)
Paula_cliente = Cliente('Paula Ochoa', 'pau8a16@gmail.com', 2)
Paula_cliente.establecer_saldo(5e10)
print(Paula_cliente.saludos())
print(Paula_usuario.saludos())
