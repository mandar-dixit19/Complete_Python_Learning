
import json

# Step 1: Create a dictionary of 3 cities and their populations
cities = {
    "Pune": 3120000,
    "Mumbai": 12400000,
    "Nagpur": 2400000
}

# Step 2: Save dictionary to 'cities.json'
with open("cities.json", "w") as file:
    json.dump(cities, file)

# Step 3: Load the JSON file
with open("cities.json", "r") as file:
    loaded_cities = json.load(file)

# Step 4: Print each city and its population
print("Cities and their populations:")
for city, population in loaded_cities.items():
    print(f"{city}: {population}")

# Step 5: Ask user for a new city and population
new_city = input("\nEnter a new city name: ")
new_population = int(input(f"Enter population of {new_city}: "))

# Step 6: Update dictionary with new city info
loaded_cities[new_city] = new_population

# Step 7: Save updated dictionary back to JSON file
with open("cities.json", "w") as file:
    json.dump(loaded_cities, file)

print("\nUpdated cities data saved to cities.json")


# problem 5
try:
    # Try to open the file in read mode
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    # If file does not exist, this block runs
    print("Filenotfound!")
