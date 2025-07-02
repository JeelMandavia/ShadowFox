class Avenger:
    def __init__(self, name, age, gender, super_power, weapon, is_leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.leader = is_leader

    def get_info(self):
        print(f"\n--- Superhero Profile: {self.name} ---")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Super Power: {self.super_power}")
        print(f"Weapon: {self.weapon}")
        leader_status = "Yes" if self.leader else "No"
        print(f"Is Leader: {leader_status}")

    def is_leader(self):
        return self.leader

captain_america = Avenger("Captain America", 100, "Male", "Super Strength", "Shield", is_leader=True)
iron_man = Avenger("Iron Man", 45, "Male", "Technology", "Armor", is_leader=True)
black_widow = Avenger("Black Widow", 35, "Female", "Superhuman", "Batons")
hulk = Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon")
thor = Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir")
hawkeye = Avenger("Hawkeye", 42, "Male", "Fighting Skills", "Bow and Arrows")

print("--- Displaying Superhero Information ---")
captain_america.get_info()
iron_man.get_info()
black_widow.get_info()
hulk.get_info()
thor.get_info()
hawkeye.get_info()

print("\n--- Checking Leader Status ---")
print(f"{captain_america.name} is a leader: {captain_america.is_leader()}")
print(f"{iron_man.name} is a leader: {iron_man.is_leader()}")
print(f"{black_widow.name} is a leader: {black_widow.is_leader()}")
print(f"{hulk.name} is a leader: {hulk.is_leader()}")
print(f"{thor.name} is a leader: {thor.is_leader()}")
print(f"{hawkeye.name} is a leader: {hawkeye.is_leader()}")

print("\n--- Listing All Leaders ---")
avengers_team = [captain_america, iron_man, black_widow, hulk, thor, hawkeye]
leaders = [avenger.name for avenger in avengers_team if avenger.is_leader()]

if leaders:
    print(f"The leaders of the Avengers are: {', '.join(leaders)}")
else:
    print("There are no designated leaders in this team.")