#author DMH 12.14.21

drivingdst = int(input("What is the the driving distance:"))

fueleff = int(input("What is the fuel efficiency:"))

price = int(input("What is the price of fuel:"))

fuel = drivingdst / fueleff

gas = fuel * price 

print(gas + "$")