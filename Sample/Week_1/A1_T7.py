#Print info message “Calculate fuel consumtion.”
print("Calculate fuel consumption.")
#Ask “Enter travel distance(kilometers): ” and store the value to Feed variable
#Convert the Feed into an integer and assign it to Distance variable
Distance = input("Enter travel distance(kilometers:")
#Ask “Enter fuel usage(liters): ”
#Convert the Feed into an integer and assign it to FuelUsage variable
FuelUsage = input("Enter fuel usage(liters):")
#Calculate the Consumption for 100 km
Consumption = int(Distance)/int(FuelUsage)
print("Fuel consumption is", Consumption, "l per 100km")


