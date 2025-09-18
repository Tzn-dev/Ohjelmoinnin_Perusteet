#Print info message “Calculate fuel consumtion.”
print("Calculate fuel consumption.")
#Ask “Enter travel distance(kilometers): ” and store the value to Feed variable
Feed = input("Enter travel distance(kilometers:")
#Convert the Feed into an integer and assign it to Distance variable
Distance = int(Feed)
#Ask “Enter fuel usage(liters): ”
#Convert the Feed into an integer and assign it to FuelUsage variable
Feed = input("Enter fuel usage(liters):")
FuelUsage = int(Feed)
#Calculate the Consumption for 100 km
#Convert the Consumption back to an integer
Consumption = (FuelUsage/Distance)*100
Consumption = int(Consumption)
#Print “Fuel consumption is {Consumption} l per 100 km”
print("Fuel consumption is",Consumption,"l per 100 km")




