import random
from colorama import Fore, Style

computer_number = random.randint(1, 100)
remaining_attempts = 20
level = 1
player_input = ""
no_attempts_remaining = False
game_won = False

print(f"Hi! Guess the computer number. Level: {level}. You can make {remaining_attempts} attempts.")

while True:

    while level == 1:
        player_input = input("Guess the number (1-100): ")

        if not player_input.isdigit():
            print("Invalid input! Try again...")
            continue

        player_number = int(player_input)

        if player_number > computer_number:
            remaining_attempts -= 1
            print(Fore.RED + "Too high!")
            print(Style.RESET_ALL)

            if remaining_attempts == 0:
                no_attempts_remaining = True
                print(f"No more attempts!")
                break
            else:
                print(f"Remaining attempts: {remaining_attempts}")

        elif player_number < computer_number:
            remaining_attempts -= 1
            print(Fore.BLUE + "Too low!")
            print(Style.RESET_ALL)

            if remaining_attempts == 0:
                no_attempts_remaining = True
                print(f"No more attempts!")
                break
            else:
                print(f"Remaining attempts: {remaining_attempts}")

        else:
            print("You guessed it!")
            level += 1
            computer_number = random.randint(1, 200)
            remaining_attempts = 15
            print(f"Level: {level}. You can make {remaining_attempts} attempts.")

        while level == 2:
            player_input = input("Guess the number (1-200): ")

            if not player_input.isdigit():
                print("Invalid input! Try again...")
                continue

            player_number = int(player_input)

            if player_number > computer_number:
                remaining_attempts -= 1
                print(Fore.RED + "Too high!")
                print(Style.RESET_ALL)

                if remaining_attempts == 0:
                    no_attempts_remaining = True
                    print(f"No more attempts!")
                    break
                else:
                    print(f"Remaining attempts: {remaining_attempts}")

            elif player_number < computer_number:
                remaining_attempts -= 1
                print(Fore.BLUE + "Too low!")
                print(Style.RESET_ALL)

                if remaining_attempts == 0:
                    no_attempts_remaining = True
                    print(f"No more attempts!")
                    break
                else:
                    print(f" Remaining attempts: {remaining_attempts}")

            else:
                print("You guessed it!")
                level += 1
                computer_number = random.randint(1, 300)
                remaining_attempts = 10
                print(f"Level: {level}. You can make {remaining_attempts} attempts.")

            while level == 3:
                player_input = input("Guess the number (1-300): ")

                if not player_input.isdigit():
                    print("Invalid input! Try again...")
                    continue

                player_number = int(player_input)

                print(f"You have {remaining_attempts} attempts.")

                if player_number > computer_number:
                    remaining_attempts -= 1
                    print(Fore.RED + "Too high!")
                    print(Style.RESET_ALL)

                    if remaining_attempts == 0:
                        no_attempts_remaining = True
                        print(f"No more attempts!")
                        break
                    else:
                        print(f" Remaining attempts: {remaining_attempts}")

                elif player_number < computer_number:
                    remaining_attempts -= 1
                    print(Fore.BLUE + "Too low!")
                    print(Style.RESET_ALL)

                    if remaining_attempts == 0:
                        no_attempts_remaining = True
                        print(f"No more attempts!")
                        break
                    else:
                        print(f" Remaining attempts: {remaining_attempts}")

                else:
                    print("You guessed it!")
                    game_won = True
                    break

    if game_won:
        print("Congrats, you win!")
        break
    if no_attempts_remaining:
        print("Sorry, you lost!")
        break
