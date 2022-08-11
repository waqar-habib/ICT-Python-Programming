"""
Week 9 Discussion
Waqar Habib
Wed, 8/10/22

"""
import glob
import os
import pandas as pandas
import matplotlib.pyplot as plt


try:
    # importing csv data from zip file using glob
    globFile = glob.glob("C:/Users/waqar/OneDrive/Desktop/Data/*.csv")
    # creating a list for the globbed data
    data = [] 
    
    # reading each csv file
    for csvFile in globFile:
        stockData = pandas.read_csv(csvFile)
        # reading by column name "symbol"
        stockData['Symbol'] = os.path.basename(csvFile)
        # appending stockData to empty list
        data.append(stockData)
        
    # converting data into pandas data frame    
    dataFrame = pandas.concat(data, ignore_index=True) 
    
    # extracting stock name from .csv
    dataFrame['Symbol'] = dataFrame['Symbol'].str.rstrip('.csv')

# exception handling
except Exception as error:
            print("Error: "+str(error))

try:
    # computing avg/std - Grouping data by col symbol and calc. by col. close
    avgSTD = dataFrame.groupby(['Symbol']).agg({'Close':['mean','std']})
    # computing average stock price/std for SPY
    stockSPY = dataFrame[dataFrame['Symbol'].str.contains("SPY")]
    # merge method
    correlationCoeff = pandas.merge(dataFrame, stockSPY, on=['Date'])
    calculateCoeff = correlationCoeff.groupby(['Symbol_x']).Close_x.corr(correlationCoeff.Close_y)
    
    #printing tables
    print(avgSTD)
    print("  ")
    print(calculateCoeff)

except Exception as error:
    print("Error:",error)

# using matplotlib to plot graph
figure,axes= plt.subplots(figsize=(10,7))

for label, date in dataFrame.groupby(["Symbol"]):
    axis = date.plot(ax = axes, kind = 'line', x='Date', y= 'Close', label= label)

plt.legend()
plt.xticks(rotation='35')
plt.title('Week 9 Discussion')
plt.xlabel("Dates")
plt.ylabel("Closing Price (USD)")
plt.show()