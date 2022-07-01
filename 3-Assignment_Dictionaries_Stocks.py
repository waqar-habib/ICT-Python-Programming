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
aapl_dict = {'symbol': "AAPL",'numberShares': 11, 'purchasePrice': 319.91, 'priceNow': 131.56}
msft_dict = {'symbol': "MSFT",'numberShares': 15, 'purchasePrice': 169.75, 'priceNow': 247.65}
tsla_dict = {'symbol': "TSLA",'numberShares': 20, 'purchasePrice': 899.94, 'priceNow': 650.28}

# for i in meta_dict:
print(meta_dict['symbol'],'-----',meta_dict['priceNow'] * meta_dict['numberShares']- meta_dict['purchasePrice'] * meta_dict['numberShares'])

print(aapl_dict['symbol'],'-----',aapl_dict['priceNow'] * aapl_dict['numberShares']- aapl_dict['purchasePrice'] * aapl_dict['numberShares'])

print(msft_dict['symbol'],'-----',msft_dict['priceNow'] * msft_dict['numberShares']- msft_dict['purchasePrice'] * msft_dict['numberShares'])

print(tsla_dict['symbol'],'-----',tsla_dict['priceNow'] * tsla_dict['numberShares']- tsla_dict['purchasePrice'] * tsla_dict['numberShares'])

seq = [x for x in meta_dict.values() if not isinstance(x, str)]
#print(min(seq))
