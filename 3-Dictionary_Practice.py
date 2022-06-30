myDictionary = {"white" : "carpet",
                "brown" : "chairs",
                "gray" : "bed"
                }

#access item in dictionary: print(dictName["key"])
#print(myDictionary["white"])

#add items to dictionary
myDictionary["green"] = "yeti"

# adding more than one item to dictionary
#1. individually
myDictionary["bedroom"] = "dresser"
myDictionary["office"] = "computer"
#2. Multiple
myDictionary['kitchen'] = ['oven', 'microwave', 'fridge']

#print(myDictionary)

#access single item using index
#create var and set equal to what you want to pull
indexItem = myDictionary['kitchen'][2]
#print(indexItem)

#values in dict don't have to be same type. Can be strings, integers or both

#below: adding items to dictionary with integers
myDictionary = {3:"itemsInKitchen", 1:"itemsInOffice"}

#prints entire dictionary with integer items
#print(myDictionary)

#print single item using the key of one of the items' values
items = myDictionary[3]
#print(items)

