#Waqar Habib

#ICT 4370
#Wed, Jul 7, 2022
#Discussion 4

# Initiating two lists for names and weights of dogs
names = ["Max", "Lucy", "Wolf", "Rex", "Buffy"]
weights = [35.4, 60.2, 12.4, 40.3, 43.1 ]

# Two empty lists to append the weight increase to
increaseYr1 = []
increaseYr2 = []

# Function that returns the weight after year 1 and year 2
def weightIncrease(weights,increaseYr1,increaseYr2):
    for index in range(len(names)):
        # multiplying by factor of 15% for year 1 
        increaseYr1.append(weights[index]+(weights[index]*0.15))
        # adding a factor of 10% for year 2 in year 1 weights
        increaseYr2.append(increaseYr1[index] + (increaseYr1[index]*0.10))

# Initializing the weightIncrease function
weightIncrease(weights,increaseYr1,increaseYr2) 

# Formatting the results
print("-"*5+
    f" Name "+
    "-"*5+ 
    f" Weight" + 
    "-"*5+ 
    f"Yr 1 Increase" + 
    "-"*5+
    "Yr 2 Increase" 
    )   
#Looping through the data
for index in range(len(names)):     
    print("-"*5+
          f" {names[index]} "+
          "-"*5+ 
          f" {weights[index]:.1f} lbs." + 
          "-"*5+ 
          f"{increaseYr1[index]:.1f} lbs." +
          "-"*5+
          f"{increaseYr2[index]:.1f} lbs."
        )
    
#Find and printing the fattestDog using the max method
fattestDog = max(weights)
indexOfFattestDog = weights.index(fattestDog)
fattestDogName = names[indexOfFattestDog]
print(f'The fattest dog is {fattestDogName.title()} with \n a weight of {fattestDog} lbs.')