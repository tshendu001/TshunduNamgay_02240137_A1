import random
import time

def game_selection():
    while True:
        print("\nHello, Welcome to the game gamers")
        print("Select a function (1-3)")
        print("1. Guess the number \n2. Rock paper scissors game \n3. Exit Program")
        
        try:
            game = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter valid number.")
            continue
        
        if game == 1:
            print("You selected Guess the number game")
            number = random.randint(1, 20)
            attempt = 0
            start_time = time.time()
            
            while True:
                try:
                    guess = int(input("Can you guess one number: "))
                    if guess < 1 or guess > 20:
                        print("Please enter a number between 1 and 20")
                        continue
                    attempt += 1
                    if guess < number:
                        print("ohh!!! Too low")
                    elif guess > number:
                        print("ohh!!! Too high")
                    else:
                        end_time = time.time()
                        print("WOW! You got it in", attempt, "attempts!")
                        print("Time taken:", round(end_time - start_time, 2), "seconds")
                        break
                except ValueError:
                    print("Enter a valid number")
        
        elif game == 2:
            print("You have selected Rock Paper Scissors game")
            print("Welcome to the Rock Paper Scissors game")
            print("1. Rock \n2. Paper \n3. Scissor")
            
            start_time = time.time()
            
            while True:
                computer = random.choice(["rock", "paper", "scissor"])
                player = input("Enter your choice: ").lower()
                
                if player not in ["rock", "paper", "scissor"]:
                    print("Invalid choice, try again")
                    continue
                
                print(f"Computer choice is {computer}")
                if player == computer:
                    print("It's a tie")
                elif (player == "rock" and computer == "scissor") or \
                     (player == "scissor" and computer == "paper") or \
                     (player == "paper" and computer == "rock"):
                    print("You won!")
                else:
                    print("You lost!")
                
                end_time = time.time()
                print("Time taken:", round(end_time - start_time, 2), "seconds")
                break
        
        elif game == 3:
            print("You have chosen to exit. Goodbye!")
            break
        else:
            print("Invalid choice, please select 1, 2, or 3.")

game_selection()
