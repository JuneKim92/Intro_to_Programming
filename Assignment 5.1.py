#Here is the dictionary of stocks I created with real-time values from Apple's stocks app.
stocks_dict = {
  "AAPL": 165.21,
  "BA": 201.71,
  "BRK-B": 319.74,
  "DIS": 99.90,
  "GE": 95.44,
  "GME": 22.46,
  "HD": 292.19,
  "NKE": 125.95,
  "SBUX": 107.47,
  "VZ": 39.22
}

print('Enter the stock symbol (e.g. APPL) or type exit to quit')
print('''For your reference, this database has:
AAPL, BA, BRK-B, DIS, GE, GME, HD, BKE, SBUX, and VZ included.
More can be added upon your request.''')
query = ''

while True:
#Cleaner print 
    query = input('\nInput: ').strip().upper()
#I added an exit command so that the user can exit when they are finished.
    if query == 'EXIT':
        break
#This part is creating the loop so that the program will continue asking the user to input a ticker until one cannot be found. 
    if query in stocks_dict:
        print(f"{query} has a stock price of {stocks_dict[query]}")
    else:
        print(f'{query} was not found in database')