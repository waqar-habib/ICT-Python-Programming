import sqlite3
import itertools

class Investor:
    #Auto assigning id to investor
    new_investor_id = itertools.count(1,1)

    def __init__(self, first_name, last_name, address, investorPhone):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.investorPhone = investorPhone
        self.stockList = []
        self.bondList = []
        self.investor_id = next(self.new_investor_id)
        
    # append investor_id to list
    def getinvestor_id(self):
        return self.investor_id

    # Method to get stocks and add to list
    def addStocks(self, stock):
        self.stockList.append(stock)

    # Method to get bond(s) and add to list
    def addBonds(self, bond):
        self.bondList.append(bond)

    # Method to return stock list
    def returnStockList(self):
        return self.stockList

    # Method to return bond list
    def returnBondList(self):
        return self.bondList
    
class Stock:
    # Creating stock ID using itertools library
    stock_id = itertools.count(1, 1)

    def __init__(self, stock_id, stock_symbol, total_shares, purchase_price, current_price, purchase_date):
        self.stock_id = stock_id
        self.stock_symbol = stock_symbol
        self.total_shares = total_shares
        self.purchase_price = purchase_price
        self.current_price = current_price
        self.purchase_date = purchase_date

    # Returns new stock id
    def get_stock_id(self):
        self.stock_id = (self.stock_id)
        return self.stock_id
    
    # Method to calculate stock gains and losses
    def calculateGainLoss(self, stock):
        try:
            # Initializing variables for loop
            gainLoss = 0
            countGain = 0
            countLoss = 0
            # Looping through lists to calculate gains/losses
            if stock.current_price > stock.currentValue:
                gainLoss = ("{:.2f}".format(((float(stock.current_price) * int(stock.total_shares))
                               - (float(stock.currentValue) * int(stock.total_shares)))))
                countGain += 1
            elif stock.current_price < stock.currentValue:
                gainLoss = ("{:.2f}".format(((float(stock.current_price) * int(stock.total_shares))
                               - (float(stock.currentValue) * int(stock.total_shares)))))
                countLoss += 1
            return gainLoss, countGain, countLoss
        except TypeError:
            print('Strings do not allow arithmetic operations')
            print('STR not allowed, only INT or FLOAT allowed.\n')

        # Method to get current gain/loss percentage
    def percentGainLoss(self, stock):
        try:
            # Looping through list to get percentages
            YoY = "{:.2f}".format((((float(stock.current_price) - float(stock.purchase_price)) /
                                               float(stock.purchase_price)) * 100))
            return YoY
        # If the datatypes from the file are not converted this exception will fire.
        except TypeError:
            print('Strings do not allow arithmetic operations')
            print('STR not allowed, only INT or FLOAT allowed.\n')

    # Method to get yearly gain/loss percentage
    def calculateYoY(self, stock):
        try:
            # Initializing list to hold yearly yields and the current date value
            import datetime as dt
            dateList = []
            todaysDate = dt.date.today()
            dateList = stock.purchase_date.split('/')
            purchase_date = dt.date(int(dateList[2]), int(dateList[0]), int(dateList[1]))
            # Looping through list to get percentages
            daysSincePurchase = (todaysDate - purchase_date).days / 365
            YoY = ("{:.2f}".format((((float(stock.current_price)
                                                - float(stock.purchase_price)) / float(stock.purchase_price)) /
                                                daysSincePurchase) * 100))
            return YoY
        # If the datatypes from the file are not converted this exception will fire.
        except TypeError:
            print('Strings do not allow arithmetic operations')
            print('STR not allowed, only INT or FLOAT allowed.\n')

class Bond(Stock):
    # getting new id for bond
    newBondID = itertools.count(1, 1)

    def __init__(self, stock_id, stock_symbol, total_shares, purchase_price, current_price, purchase_date,
                 coupon, YoY):
        super().__init__(stock_id, stock_symbol, total_shares, purchase_price, current_price, purchase_date)
        self.coupon = coupon
        self.YoY = YoY

    # Returns a new bond id
    def getBondID(self):
        self.stock_id = next(self.newBondID)
        return self.stock_id

# This function decides there was a max gain or min loss
# Then according to which scenario fits, the symbol matching the criteria
# is returned.
def highestGainLoss(gainsCount, countLoss):
    
    try:
        # Initializing variables for loop
        priceDifference = []
        maxGainSymbol = ''
        minLossSymbol = ''
        index = 0
        # Loop to find max gain symbol
        # If the gain counter is greater than or equal to three, symbolizing
        # a majority gain, then the loop stores all the stock price
        # differences in a list where the max function is used to find the
        # stock symbol with the maximum gain in value
        if gainsCount >= 3:
            for stock in allStocks:
                priceDifference.append(float(stock.current_price) - float(stock.purchase_price))
                index += 1
            maximumGain = max(priceDifference)
            indexOfHighestGain = priceDifference.index(maximumGain)
            index = 0
            for stock in allStocks:
                if indexOfHighestGain == index:
                    maxGainSymbol = stock.stock_symbol
                index += 1
            return("The stock with the highest increase in value\nin your portfolio on a per-share basis is: "
                   + str(maxGainSymbol))
        # Loop to find min loss symbol
        # If the loss counter is greater than or equal to three, symbolizing
        # a majority loss, then the loop stores all the stock price
        # differences in a list where the min function is used to find the
        # stock symbol with the minimum loss in value
        elif countLoss >= 3:
            for stock in allStocks:
                priceDifference.append(float(stock.purchase_price) - float(stock.current_price))
                index += 1
            minimumLoss = min(priceDifference)
            indexOfMinLoss = priceDifference.index(minimumLoss)
            index = 0
            for stock in allStocks:
                if indexOfMinLoss == index:
                    minLossSymbol = stock.stock_symbol
                index += 1
            return("The stock with the minimum loss in value\nin your portfolio on a per-share basis is: "
                   + str(minLossSymbol))
    # If the datatypes from the file are not converted this exception will fire.
    except TypeError:
        print('Cannot do mathematical operations on type: STR')
        print('Convert STR values from file to INT or FLOAT.\n')

# Function to write output to stock_output.txt file
def returnResult(stockList, bondList):

    # Printing the stock output
    print('Stock ownership for: ' + initialInvestor.first_name + " " + initialInvestor.last_name)
    print(f"{'Investor ID: ' + str(initialInvestor.getinvestor_id()):<12}{'':<2}"
          f"{'Investor Address: ' + initialInvestor.address:<12}"
          f"{'':<2}{'Phone Number: ' + initialInvestor.investorPhone:<12}")
    # Printing line of hyphens
    print("-" * 100)
    print(f"{'Stock ID':<12}{'stock_symbol':<12}{'Shares':<12}{'Gain/Loss ($)':<12}{'Gain/Loss (%):'}"
          f"{'':<2}{'% YoY:'}")
    # Printing line of hyphens
    print("-" * 100)

    # Getting variables ready for loop
    countGain = 0
    countLoss = 0

    # Looping through stock list to call functions with Stock object
    for stock in allStocks:
        # Calling class functions
        valueOfGainLoss, gainValue, lossValue = stock.calculateGainLoss(stock)
        YoY = stock.percentGainLoss(stock)
        yearly_YoY = stock.calculateYoY(stock)
        # Getting gain/loss counter values
        if gainValue == 1:
            countGain += 1
        if lossValue == 1:
            countLoss += 1
        # Printing stock info
        print(f"{stock.get_stock_id():<12}{stock.stock_symbol:<12}{stock.total_shares:<12}"
              f"{'$' + str(valueOfGainLoss):<12}{'':<5}{'%' + str(YoY):<17}"
              f"{'':<5}{'%' + str(yearly_YoY)}")

    # Printing line of hyphens
    print("-" * 100)
    # Calling max gain/loss function
    print(highestGainLoss(countGain, countLoss))

    # writing the bond output
    print('')
    print('Bond ownership for: ' + initialInvestor.first_name + " " + initialInvestor.last_name)
    print(f"{'Investor ID: ' + str(initialInvestor.getinvestor_id()):<12}"
          f"{'':<2}{'address: ' + initialInvestor.address:<12}"
          f"{'':<2}{'Phone Number: ' + initialInvestor.investorPhone:<12}")
    # Printing a line of hyphens
    print("-" * 100)
    print(f"{'Bond ID':<12}{'Symbol':<12}{'Shares':<12}{'Purchase Price':<12}"
          f"{'':<3}{'Current Price:'}{'':<2}{'Coupon:'}{'':<3}{'Yield: %'}")
    # Printing a line of hyphens
    print("-" * 100)

    # Looping through bond list with bond object
    for bond in allBonds:
        print(f"{bond.getBondID():<12}{bond.stock_symbol:<12}{bond.total_shares:<12}"
              f"{bond.purchase_price:<12}{'':<5}{bond.current_price:<15}{'':<1}"
              f"{bond.coupon:<11}{bond.YoY}")

    # Printing a line of hyphens
    print("-" * 100)

initialInvestor = Investor('Bob', 'Smith', '5566 Gooseberry Court, Seattle, Washington 45674', '555-666-777')
# Setting file names
stockFile = 'Desktop/6-stocks.csv'
bondFile = 'Desktop/6-bonds.csv'
# Getting lists ready for the loop
split = []
allStocks = []
allBonds = []

try:
    # Trying to open the stock file
    with open(stockFile) as file_object:
        # Starting with second line of file
        next(file_object)
        # Splitting the lines by attribute
        for line in file_object:
            split = line.split(',')
            initialInvestor.addStocks(Stock(0, split[0].strip('\n'), split[1].strip('\n'), split[2].strip('\n'),
                                         split[3].strip('\n'), split[4].strip('\n')))
# If the file doesn't exist this exception will fire
except FileNotFoundError:
    print(stockFile + " doesn't exist.")
    print('Ensure that the file path is correct')

# Exception handling for non_existing file
try:
    # Trying to open the bonds file
    with open(bondFile) as file_object:
        # Starting with second line of file
        next(file_object)
        # Splitting the lines by attribute
        for line in file_object:
            split = line.split(',')
            initialInvestor.addBonds(Bond(0, split[0].strip('\n'), split[1].strip('\n'), split[2].strip('\n'),
                                       split[3].strip('\n'), split[4].strip('\n'), split[5].strip('\n'),
                                       split[6].strip('\n')))
# If the file doesn't exist this exception will fire
except FileNotFoundError:
    print(bondFile + " doesn't exist.")
    print('Ensure that the file path is correct.')

# returning stock list for investments
allStocks = initialInvestor.returnStockList()
# returning bond list for investments
allBonds = initialInvestor.returnBondList()

# ----------------------------------------start of database section-------------------------------------------------#
db_connection = sqlite3.connect('test_db.db')
cursor = db_connection.cursor()

# Stored sql statements to create tables
createInvestorTable = """ CREATE TABLE IF NOT EXISTS investor (
                                 investor_id integer PRIMARY KEY,
                                 first_name text NOT NULL,
                                 last_name text NOT NULL,
                                 address text NOT NULL,
                                 phone_number text NOT NULL); """

createStockTable = """ CREATE TABLE IF NOT EXISTS stock (
                              stock_id integer PRIMARY KEY,
                              investor_id integer NOT NULL,
                              stock_symbol text NOT NULL,
                              total_shares integer NOT NULL,
                              purchase_price real NOT NULL,
                              current_price real NOT NULL,
                              purchase_date text NOT NULL); """

createBondTable = """ CREATE TABLE IF NOT EXISTS bond (
                            bond_id integer PRIMARY KEY,
                            investor_id integer NOT NULL,
                            bond_symbol text NOT NULL, 
                            total_bonds integer NOT NULL,
                            purchase_price real NOT NULL,
                            current_price real NOT NULL,
                            purchase_date text NOT NULL,
                            coupon_value real NOT NULL,
                            YoY real NOT NULL); """

# Stored sql statements to retrieve data from tables
selectInvestorName = """ SELECT * FROM investor; """

selectStockSymbol = """ SELECT * FROM stock; """

selectBondName = """ SELECT * FROM bond; """

# Executing stored sql queries
cursor.execute(createInvestorTable)
cursor.execute(createStockTable)
cursor.execute(createBondTable)

# Inserting investor info into the db
cursor.execute("""INSERT OR REPLACE INTO investor(investor_id, first_name, last_name, address, phone_number)
               VALUES (?,?,?,?,?)""", (int(initialInvestor.getinvestor_id()), str(initialInvestor.first_name),
                                       str(initialInvestor.last_name), str(initialInvestor.address),
                                       str(initialInvestor.investorPhone),))
db_connection.commit()

# Inserting stock data into the database
for stock in allStocks:
    cursor.execute("""INSERT OR REPLACE INTO stock(stock_id, investor_id, stock_symbol, total_shares, purchase_price,
                   current_price, purchase_date) 
                   VALUES (?,?,?,?,?,?,?)""", (int(stock.get_stock_id()),
                                               int(initialInvestor.getinvestor_id()),
                                               str(stock.stock_symbol),
                                               int(stock.total_shares),
                                               float(stock.purchase_price),
                                               float(stock.current_price),
                                               str(stock.purchase_date), ))
db_connection.commit()

# Inserting bond data into the database
for bond in allBonds:
    cursor.execute("""INSERT OR REPLACE INTO bond (bond_id, investor_id, bond_symbol, total_bonds, purchase_price,
                      current_price, purchase_date, coupon_value, YoY) 
                      VALUES (?,?,?,?,?,?,?,?,?)""", (int(bond.getBondID()),
                                                      int(initialInvestor.getinvestor_id()),
                                                      str(bond.stock_symbol),
                                                      int(bond.total_shares),
                                                      float(bond.purchase_price),
                                                      float(bond.current_price),
                                                      str(bond.purchase_date),
                                                      float(bond.coupon),
                                                      float(bond.YoY), ))

db_connection.commit()

# Getting investor info from db
cursor.execute(selectInvestorName)
investorInfo = cursor.fetchall()

# Getting stock info from db
cursor.execute(selectStockSymbol)
stockInfo = cursor.fetchall()
# Making stock objects
stockDB = []
for stock in stockInfo:
    stockDB.append(Stock(stock[0], stock[2], stock[3], stock[4], stock[5], stock[6]))

# Getting bond info from db
cursor.execute(selectBondName)
bondInfo = cursor.fetchall()
# Making bond objects
bondDB = []
for bond in bondInfo:
    bondDB.append(Bond(bond[0], bond[2], bond[3], bond[4], bond[5], bond[6], bond[7], bond[8]))

# Closing the db connection
db_connection.close()

# Calling print output function
returnResult(stockDB, bondDB)