while True:

    print('''
    *******************************************************************************
              |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |  ___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

    direction = input("You have reached the island. There is a path to the left, and a path to the right. Which do you choose, Left or Right?\n")
    lower_direction = str.lower(direction)
    if lower_direction == "left":
        print("You have made it safely down the path.\n")
        wait_swim = input("You have reached a small lake on the island, and you need to cross. There is a boat available at some point. Do you wait for the boat or swim across? Which do you choose, wait, or swim?\n")
        lower_wait_swim = str.lower(wait_swim)
        if lower_wait_swim == "wait":
            print("The boat brings you safely across the lake.\n")
            rby_str = input("You have reached a small house, and you enter. There are three doorss: yellow, red, and blue. Which door do you choose, Yellow, Red, or Blue?\n")
            rby = str.lower(rby_str)
            if rby == "red":
                print("You are engulfed in flames and die in a blaze! GAME OVER.")
                check_str = input("Do you want to CONTINUE and start over? Y or N\n")
                check = str.lower(check_str)
                if check == "y":
                    continue
                elif check == "n":
                    print("Bye..")
                    break
            elif rby == "blue":
                print("The room is full of rabid wild beasts who eat you! GAME OVER.")
                check_str = input("Do you want to CONTINUE and start over? Y or N\n")
                check = str.lower(check_str)
                if check == "y":
                    continue
                elif check == "n":
                    print("Bye..")
                    break
            elif rby == "yellow":
                print("You enter a room full of amazing treasure!! You win!")
                check_str = input("Do you want to CONTINUE and start over? Y or N\n")
                check = str.lower(check_str)
                if check == "y":
                    continue
                elif check == "n":
                    print("Bye..")
                    break
        elif lower_wait_swim == "swim":
            print("Oh no.. an alligator eats you for a snack.. GAME OVER.")
            check_str = input("Do you want to CONTINUE and start over? Y or N\n")
            check = str.lower(check_str)
            if check == "y":
                continue
            elif check == "n":
                    print("Bye..")
                    break
    elif lower_direction == "right":
        print("Oh no! You fell into a pit with spikes! GAME OVER")
        check_str = input("Do you want to CONTINUE and start over? Y or N\n")
        check = str.lower(check_str)
        if check == "y":
            continue
        elif check == "n":
                    print("Bye..")
                    break
