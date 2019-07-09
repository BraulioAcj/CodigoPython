#Un modulo es basicamente un archivo que contiene un conjunto de funciones

import datetime
hoy = datetime.date.today()
print(hoy)

from datetime import date
hoy2 = date.today()
print(hoy2)

import time
estampatemporal = time.time()
print(estampatemporal)

from time import time
estampatemporal2 = time()
print(estampatemporal2) 

#modulo personalizado
import validador 
from validador import validate_email

email='prueba@prueba.es'
if validate_email(email):
	print('El correo esta bien escrito')
else:
	print('El correo esta mal escrito')
