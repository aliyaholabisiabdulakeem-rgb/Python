driving_distance = float(input("Enter the driving distance"))
fuel_efficiency = float(input("Enter the miles per gallon"))
price_per_gallon = float(input("Enter the price per gallon used"))

cost_of_driving = ((driving_distance / fuel_efficiency) * price_per_gallon)

cost_of_driving = round(cost_of_driving, 2)

print("The cost of driving is $", cost_of_driving)