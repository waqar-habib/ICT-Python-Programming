#Waqar Habib

#ICT 4370
#Wed, Jun 22, 2022
#Discussion 2

# Initiating two lists
dogName = ["Max", "Lucy", "Wolf", "Rex", "Buffy"]
dogWeight = [35.5, 60.2, 12.4, 40.3, 43.1 ]

#Find the fattestDog using the max method
fattestDog = max(dogWeight)
indexOfFattestDog = dogWeight.index(fattestDog)
fattestDogName = dogName[indexOfFattestDog]
 
# Table Format

# Header
print('\n Dogs and their weights in lbs:')
print('_'*32)

#Format each dog name and corresponding dog weight:
for index, singleDog in enumerate(dogName):
    print((f'|{singleDog.title()}') +'-' * (20-len(singleDog)) + f'|{dogWeight[index]} lbs.|')

# print separating line
print('_'*32)

#calculates the index of dog name/weight
fattestDogName = dogName[dogWeight.index(max(dogWeight))]
print(f'The fattest dog is {fattestDogName.title()} with \n a weight of {fattestDog} lbs.')

# print separating line
print('_'*32)

#For loop for rows
index = 0
for x in dogName:
    spacesRow = 12-len(dogName[index])
    name = dogName[index]
    weight = {dogWeight[index]}
    index += 1

