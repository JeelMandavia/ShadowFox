import random
def dice_rolls(num_rolls=20):
    rolls = []
    rolls_6 = 0
    rolls_1 = 0
    two_6s_in_row = 0
    print(f"Total {num_rolls} dice rolls:")
    for i in range(num_rolls):
        roll = random.randint(1, 6)
        rolls.append(roll)
        print(f"Roll {i+1}: {roll}")
        if roll == 6:
            rolls_6 += 1
        if roll == 1:
            rolls_1 += 1
        if i > 0 and rolls[i-1] == 6 and roll == 6:
            two_6s_in_row += 1
    print("\nDice Roll Statistics: \n")
    print(f"Total rolls: {num_rolls}")
    print(f"Times rolled a 6: {rolls_6}")
    print(f"Times rolled a 1: {rolls_1}")
    print(f"Times rolled two 6s in a row: {two_6s_in_row}")
dice_rolls()