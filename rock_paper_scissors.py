rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
while True:
    player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
    if player_choice == "0":
        print(rock)
        print("Computer chose:")
        random_computer_choice = random.randint(0, 2)
        if random_computer_choice == 0:
            print(rock)
            print("You tie.")
            check = input("Start over? Y or N\n").lower()
            if check == "y":
                continue
            elif check == "n":
                print("Bye..")
                break
            else:
                print("Bye..")
                break
        elif random_computer_choice == 1:
            print(paper)
            print("You lose.")
            check = input("Start over? Y or N\n").lower()
            if check == "y":
                continue
            elif check == "n":
                print("Bye..")
                break
            else:
                print("Bye..")
                break
        elif random_computer_choice == 2:
            print(scissors)
            print("You win!")
            check = input("Start over? Y or N\n").lower()
            if check == "y":
                continue
            elif check == "n":
                print("Bye..")
                break
            else:
                print("Bye..")
                break

    elif player_choice == "1":
        print(paper)
        print("Computer chose:")
        random_computer_choice = random.randint(0, 2)
        if random_computer_choice == 0:
            print(rock)
            print("You win!")
            check = input("Start over? Y or N\n").lower()
            if check == "y":
                continue
            elif check == "n":
                print("Bye..")
                break
            else:
                print("Bye..")
                break
        elif random_computer_choice == 1:
            print(paper)
            print("You tie.")
            check = input("Start over? Y or N\n").lower()
            if check == "y":
                continue
            elif check == "n":
                print("Bye..")
                break
            else:
                print("Bye..")
                break
        elif random_computer_choice == 2:
            print(scissors)
            print("You lose.")
            check = input("Start over? Y or N\n").lower()
            if check == "y":
                continue
            elif check == "n":
                print("Bye..")
                break
            else:
                print("Bye..")
                break

    elif player_choice == "2":
        print(scissors)
        print("Computer chose:")
        random_computer_choice = random.randint(0, 2)
        if random_computer_choice == 0:
            print(rock)
            print("You lose.")
            check = input("Start over? Y or N\n").lower()
            if check == "y":
                continue
            elif check == "n":
                print("Bye..")
                break
            else:
                print("Bye..")
                break
        elif random_computer_choice == 1:
            print(paper)
            print("You win!")
            check = input("Start over? Y or N\n").lower()
            if check == "y":
                continue
            elif check == "n":
                print("Bye..")
                break
            else:
                print("Bye..")
                break
        elif random_computer_choice == 2:
            print(scissors)
            print("You tie.")
            check = input("Start over? Y or N\n").lower()
            if check == "y":
                continue
            elif check == "n":
                print("Bye..")
                break
            else:
                print("Bye..")
                break
    else:
        print("Invalid number..")
        check = input("Start over? Y or N\n").lower()
        if check == "y":
          continue
        elif check == "n":
          print("Bye..")
          break
        else:
          print("Bye..")
          break
