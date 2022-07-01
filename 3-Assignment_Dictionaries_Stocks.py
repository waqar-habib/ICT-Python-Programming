#Waqar Habib

#ICT 4370
#Thu, Jun 30, 2022
#Assignment 3

from curses import meta
from operator import itemgetter


print("Part One - Dictionary")
# previous lists to dictionary

myPortfolio = [{
    'stockSymbol': 'META',
    'numberShares': 10,
    'purchasePrice': 325.20,
    'priceNow': 163.74
    },
    {
    'symbol': 'META',
    'numberShares': 10,
    'purchasePrice': 325.20,
    'priceNow': 163.74
    },
    {
    'symbol': 'MSFT',
    'numberShares': 15,
    'purchasePrice': 169.75,
    'priceNow': 247.65
    },
    {
    'symbol': 'TSLA',
    'numberShares': 20,
    'purchasePrice': 899.94,
    'priceNow': 650.28
    }               
]

#create separate dicts for each symbol

meta_dict = {'symbol': "META",'numberShares': 10, 'purchasePrice': 325.20, 'priceNow': 163.74}
aapl_dict = {'numberShares': 11, 'purchasePrice': 319.91, 'priceNow': 131.56}
msft_dict = {'numberShares': 15, 'purchasePrice': 169.75, 'priceNow': 247.65}
tsla_dict = {'numberShares': 20, 'purchasePrice': 899.94, 'priceNow': 650.28}

# for i in meta_dict:
print(meta_dict['symbol'],':',meta_dict['priceNow'] * meta_dict['numberShares']- meta_dict['purchasePrice'] * meta_dict['numberShares'])
    
# for i in meta_dict:
#     print(aapl_dict[i])    

# for i in msft_dict:
#     print(msft_dict[i])  

# for i in tsla_dict:
#     print(tsla_dict[i])  

#x=5
#print("I want",x+3,"slices of pizza!")

seq = [x for x in meta_dict.values() if not isinstance(x, str)]
print(min(seq))
