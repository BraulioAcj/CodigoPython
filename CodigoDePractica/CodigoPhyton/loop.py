#Simple	loop
people = ['Paula','Ana','Jorge','Mau','Braulio']
print('Simple loop')
for person in people:
        print('Current Person: {0}'.format(person))

#Break
print('***Break loop***')
for person in people:
  if person=='Mau':
     break
  print('Current Person: {0}'.format(person))

#Continue
print('***Continue loop***')
for person in people:
   if person=='Mau':
	continue
   print('Current Person: {0}'.format(person))
   print('Hola mundo otra vez')

#range
for i in range(len(people)):
	print(people[i])

for i in range(0,11):
	print('number: {0}'.format(i))
	print('orden extra para ver la importancia de indentacion')


#while loops: hasta que se cumpla una condicion
count=0
while count<=7:
	print('count: {0}'.format(count))
	count+=1

