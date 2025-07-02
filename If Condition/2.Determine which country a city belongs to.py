print("Here is the list of cities of different countries:\n")
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Banglore", "Chennai", "Delhi"]
print(f"Australia : {australia}")
print(f"UAE : {uae}")
print(f"India : {india}")
city = input("\nEnter a city name from the list of any country: ")
if city in australia:
    print(f"{city} is in Australia.")
elif city in uae:
    print(f"{city} is in UAE.")
elif city in india:
    print(f"{city} is in India.")
else:
    print(f"{city} was not found in the given lists.")