import random
  
# Game Start Display
def menu():
    print("\t  <MASTERMIND GAME>")
    print("\n\t   Start Game   [1]")
    print("\t   How to play? [2]")
    print("\t   Exit Game    [3]")

# User input for either command
menu()
gcmd=int(input("\n\t   Enter a number: "))

while gcmd != 3:
    if gcmd == 2:
        # Check if User enter 2 to view instructions
        print("\n\t  <How to Play> \n")
        print("\nMastermind is a two-player code-breaking game in which one player hides a random code")
        print("consisting of colours while the other player has to guess it using clues given by the user for each turn.")
        print("\nThe code can be made up of any combination of the colours RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE")  
        print("(Enter input as RED=R. GREEN=G, BLUE=B, YELLOW=Y, ORANGE=O, PURPLE=P) ")
        print("Computer will automatically generate four random colours from list.")
        print("If the system prints out an X it means the colour is correct and in the right place")
        print("If the system prints out an o it means the colour is correct but in the wrong place")
        print("If the system prints out nothing it means the colour is wrong")
        print("Player must guess 4 colours numbers correctly from the list to win")
        gcmd=input("\n\t   Enter [1] or [3] to reutrn to menu: ")

    elif gcmd ==1:
        # List of possible colours
        # game start
        colours = ["R", "G", "B", "Y", "O", "P"]
        attempts = 0
        game = True

        # computer randomly picks four colour code
        colour_code = random.sample(colours,4)
        print(colour_code)	
        print("Game start! Enter 4 colours")
        print("RED=R. GREEN=G, BLUE=B, YELLOW=Y, ORANGE=O, PURPLE=P")
        # player guesses the number	
        while game:
            
            correct_colour = ""
            guessed_colour = ""
            player_guess = input().upper()
            attempts += 1
            
            # checking if player's input is correct
            if len(player_guess) != len(colour_code):
                print ("\nThe secret code has exactly four colours, so don't enter more or less than four!")
                continue
            for i in range(1):
                if player_guess[i] not in colours:
                    print ("\nPlease enter a valid colour: RED=R. GREEN=G, BLUE=B, YELLOW=Y, ORANGE=O, PURPLE=P")
                    continue
                    
            # comparison between user input & computer
            if correct_colour != "XXXX":
                for i in range(4):
                    if player_guess[i] == colour_code[i]:
                        correct_colour += "X"
                    if  player_guess[i] != colour_code[i] and player_guess[i] in colour_code:
                        guessed_colour += "O"
                print (correct_colour +  guessed_colour + "\n")		
                
            if correct_colour == "XXXX":
                if attempts == 1:
                    print ("You guessed the code on your first try!")
                    game = False
                else:
                    print ("You did it ! You needed " + str(attempts) + " attempts to guess.")
                    game = False
            elif attempts >= 1 and attempts <=10 and correct_colour != "XXXX":
                 print ("Next attempt: ")
            else:
                    print ("You failed ! The secret colour code was: " + str(colour_code) + " Better luck next time !")
                    game = False

            # replay
            while game == False:
                replay = input("\nDo you want to play again? (Y/N)").upper()	
                attempts = 0
                if replay =="N":
                    print ("Thank you for playing!")
                    exit()
                elif replay == "Y":
                    print("Starting game again")
                    print("Game start! Enter 4 colours")
                    print("RED=R. GREEN=G, BLUE=B, YELLOW=Y, ORANGE=O, PURPLE=P")
                    game = True
                    colour_code = random.sample(colours,4)
                    print(colour_code)
                else:
                    print("Invalid input, enter Y/N")
                    
    else:
        print("Invalid input, please enter 1, 2 or 3")

    print()
    menu()
    gcmd=int(input("\n\t   Enter a number: "))
print("Now exiting")
exit()

