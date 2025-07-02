print("The program checks if two names of the city given are of same country or not:")
print("Here is the list of cities of different countries:\n")
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Banglore", "Chennai", "Delhi"]
print(f"Australia : {australia}")
print(f"UAE : {uae}")
print(f"India : {india}")
city_one = input("\nEnter the first city: ")
city_two = input("Enter the second city: ")
if city_one in australia and city_two in australia:
    print(f"\n{city_one} and {city_two} both belongs to Australia.")
elif city_one in uae and city_two in uae:
    print(f"\n{city_one} and {city_two} both belongs to UAE.")
elif city_one in india and city_two in india:
    print(f"\n{city_one} and {city_two} both belongs to India.")
else:
    print(f"\n{city_one} and {city_two} does not belong to same country.")