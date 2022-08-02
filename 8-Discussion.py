import json
import pygal
from pygal.style import Style

filePath = 'dogWeights.json'
with open(filePath) as file:
    data = json.load(file)

dateList = []
nameSet = set()
idSet = set()
dogsList = {}

for item in data:
    if item['Date'] not in dateList:
        dateList.append(item['Date'])
        
    if item['DogID'] not in idSet:
        idSet.add(item['DogID'])
        nameSet.add(item['Dog'])
        dogsList[item['Dog']] = []
        dogsList[item['Dog']].append(item['Weight'])
    
    while len(dogsList[item['Dog']]) < len(dateList):
        dogsList[item['Dog']].insert(0, None)

# customizing colors        
custom_style = Style(
    colors=('#800000', '#000080', '#CC5500'))

# Creating chart
graph = pygal.Line(height=400, width = 300, style=custom_style)
graph.title = 'Weight Over Time'


graph.x_labels = map(str, dateList)

for name in nameSet:
    graph.add(name, dogsList[name])
graph.render_to_file('graph.svg')
print("Graph Rendered Sucessfully!")