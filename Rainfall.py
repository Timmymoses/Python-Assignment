int_str = input("Enter the inch of rainfall: ")

acre_str = input("Enter the number of acre: ")
acre_int = int(acre_str)

gallon = 6272640 * acre_int / 231


print("There are ", gallon , "gallons in" , acre_int, "acres of land")