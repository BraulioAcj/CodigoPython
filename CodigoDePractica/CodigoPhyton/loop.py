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
#print('***Continue loop***')
#for persob in people:
#   if person=='Mau':
