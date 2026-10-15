getinterest = lambda amount,rate,year : (amount * rate * year) /100
celsiustofahrenheit = lambda celsius : (celsius *(9/5))+32
amount = float(input("Enter the amount:"))
rate = float (input("Enter the rate:"))
year = float(input("Enter the year:"))

celsius = float(input("Enter temperature in celsius: "))

print(getinterest(amount,rate,year))

print(celsiustofahrenheit(celsius))
