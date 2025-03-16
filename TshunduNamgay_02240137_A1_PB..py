import random
import time

def game_to_be_selected():
    while True:
        print("\nHello, Welcome to the game gamers")
        print("Select a function (1-3)")
        print("1. Guess the number as you want\n2. Rock paper scissors game \n3. exit Program")
        
        try:
            paly = int(input("Please_enter_your_choice: "))
        except ValueError:
            print("Please enter valid number.")
            continue
        
        if paly == 1:
            print("You have selected guess the number game")
            nums = random.randint(1, 20)
            tryed = 0
            begin_the_time = time.time()
            
            while True:
                try:
                    guess = int(input("Can you guess one number: "))
                    if guess < 1 or guess > 20:
                        print("Please enter a number between 1 and 20")
                        continue
                    tryed += 1
                    if guess < nums:
                        print("ohh!!! Too LOW")
                    elif guess > nums:
                        print("ohh!!! Too HIGH")
                    else:
                        end_time = time.time()
                        print("WOW! You got it in", tryed, "Attempts!!!")
                        print("Time_you_had_taken:", round(end_time - begin_the_time, 2), "Seconds")
                        break
                except ValueError:
                    print("Please enter a valid number")
        
        elif paly == 2:
            print("You_have_selected_the_Rock_Paper_Scissors_game")
            print("Welcome_to_the_Rock_Paper_Scissors_game")
            print("1.ROCK \n2. PAPER \n3.SCISSOR")
            
            begin_the_time = time.time()
            
            while True:
                degital = random.choice(["rock", "paper", "scissor"])
                gamer = input("Enter your choice: ").lower()
                
                if gamer not in ["rock", "paper", "scissor"]:
                    print("Invalid choice, try again")
                    continue
                
                print(f"desital give as choice is {degital}")
                if gamer == degital:
                    print("It's a tie")
                elif (gamer == "rock" and degital == "scissor") or \
                     (gamer == "scissor" and degital == "paper") or \
                     (gamer == "paper" and degital == "rock"):
                    print("You__won!!!")
                else:
                    print("You__lost!!!")
                
                end_time = time.time()
                print("The_Time_ taken:", round(end_time - begin_the_time, 2), "Seconds")
                break
        
        elif paly == 3:
            print("You have opt to the exit. Goodbye! we had a good game!")
            break
        else:
            print("you have an invilied, can you please select the value 1, 2, or 3.")

game_to_be_selected()
