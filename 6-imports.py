#Waqar Habib

#ICT 4370
#Wed, Jul 20, 2022
#Discussion 6

class DogsAndWeights:
    def __init__(self, dogName, dogWeight):
        self.dogName = dogName
        self.dogWeight = dogWeight

    # Calculate increase in weight
    def increaseInWeight(self, dogWeight):
        increaseYr1 = (float(self.dogWeight))+(float(self.dogWeight)* 0.15)
        increaseYr2 = (float(increaseYr1))+(float(increaseYr1)* 0.10)
        return (round(increaseYr1,2)), (round(increaseYr2,2))
    
# File name as a var that can be called in the with open function
csvFile = 'ICT-Python-Programming/ICT-Python-Programming/Dogs_Week6.csv'

# Two empty lists to append data to
dogName = []
dogWeights = []

# Error Handling
try:
    # with open reads file and 
    with open(csvFile) as csvTable:
        # Skipping the first line in the csvTable
        next(csvTable)
        # Using "," as a delimiter to separate dog names and dog weights
        for line in csvTable:
            delimiter = line.split(',')
            # Stripping empty spaces using rstrip function
            dogName.append(delimiter[0].rstrip('\n'))
            dogWeights.append(delimiter[1].rstrip('\n'))
    
    # Empty list to append dog names and dog weights        
    dogList = []

    # Looping through the data and appending dog names and dog weights to dogList
    for i in range(len(dogName)):
        dogList.append(DogsAndWeights(dogName[i], dogWeights[i]))

    # Finding who the fattest dog is
    maxWeight = max(dogWeights)
    fattestDog = ''

    print(" ")
    print(f"{'Name'}\t\t{'Current'}\t\t{'Year 1'}\t\t{'Year 2'}")

    # Loop through dogList for individual dog weights
    for dog in dogList:
        yr1Weight, yr2Weight = dog.increaseInWeight(dog.dogWeight)
        
        # Printing table
        print(f"{dog.dogName} \t \t {dog.dogWeight} \t\t {yr1Weight} \t\t {yr2Weight}")
        
        if dog.dogWeight == maxWeight:
            fattestDog = dog.dogName

    # Printing who the fattest dog is
    print("")
    print("The heaviest dog of the bunch is " + fattestDog)
    print("")
    
except FileNotFoundError:
    print("")
    print("The file "+ csvFile + " does not exist. Please check the file path and try again.")
    print("")
    