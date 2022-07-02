#lists inside dictionary


myStocks = {
    'META': [10, 325.20, 163.74 ],
    'AAPL': [11, 319.91, 131.56 ],
    'MSFT': [15, 169.75, 247.65 ],
    'TSLA': [20, 899.94, 650.28 ],   
}

#for loop

for symbol, x in myStocks.items():
    print(f"\n{symbol}")
    for y in x:
        print(f"\n{y}")
        


'''
favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
        
        '''