def jumping_jack_workout_for_loop():
    total_jacks_target = 100
    jacks_per_set = 10
    jacks_completed = 0

    num_sets = total_jacks_target // jacks_per_set

    print("--- Jumping Jack Workout Routine ---")
    print(f"Your goal is to complete {total_jacks_target} jumping jacks.")

    for set_num in range(num_sets):
        current_set_jacks = min(jacks_per_set, total_jacks_target - jacks_completed)

        jacks_completed += current_set_jacks
        print(f"\n--- SET {set_num + 1} ---")
        print(f"Perform {current_set_jacks} jumping jacks now!")
        print(f"You have now completed a total of {jacks_completed} jumping jacks.")

        if jacks_completed < total_jacks_target:
            tired_response = input("Are you tired? (yes/no): ").lower()

            if tired_response in ['yes', 'y']:
                skip_response = input("You feel tired. Do you want to skip the remaining sets? (yes/no): ").lower()
                if skip_response in ['yes', 'y']:
                    print(f"\nOkay, workout ended. You completed a total of {jacks_completed} jumping jacks.")
                    break
                elif skip_response in ['no', 'n']:
                    remaining_jacks = total_jacks_target - jacks_completed
                    print(f"Great! You have {remaining_jacks} jumping jacks remaining. Keep going!")
                else:
                    print("Invalid response for skipping. Continuing workout.")
                    remaining_jacks = total_jacks_target - jacks_completed
                    print(f"You have {remaining_jacks} jumping jacks remaining.")

            elif tired_response in ['no', 'n']:
                remaining_jacks = total_jacks_target - jacks_completed
                print(f"That's the spirit! You have {remaining_jacks} jumping jacks remaining.")
            else:
                print("Invalid response. Please type 'yes' or 'no'. Continuing workout.")
                remaining_jacks = total_jacks_target - jacks_completed
                print(f"You have {remaining_jacks} jumping jacks remaining.")
    else:
        print("\nCongratulations! You completed the workout!")

jumping_jack_workout_for_loop()