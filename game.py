import random;

def getHello():
    print("Welcome to Rock-Paper-Scissors game!")
    print("Winning Rules:")
    print("Rock vs Paper -> Paper wins")
    print("Rock vs Scissors -> Rock wins")
    print("Paper vs Scissors -> Scissors wins")

    choices = ["rock", "paper", "scissors"]

    while True:
        print("\nChoose an option: Rock, Paper, or Scissors")

        try:
            user_choice = input("Please enter your choice: ").strip().lower()
            if  user_choice not in choices:
                raise ValueError("ERROR: invalid value")  
            
                   
        except ValueError:
            print("Please enter the valid value")
            continue

        comp_choice = random.choice(choices)
        
        print('\nUser choice is: ', user_choice)
        print("Now it is Computers's Turn... ")
        print("Computers's choice is: ", comp_choice)

        if user_choice == comp_choice:
            print("It is a Tie!")
        elif (
            (user_choice == "paper" and comp_choice ==  "rock") or
            (user_choice == "scissors" and comp_choice ==  "paper") or
            (user_choice == "rock" and comp_choice ==  "scissors")
        ):
            print("<== User Wins! ==>")
        else:
            print("<== Computer Wins! ==>")

        while True:
            answer = input("\nDo you want to play again? (y/n)").lower()
        
            if answer in ['y', 'n']:
                break
            
            print("Please enter y or n")
        
        if answer == 'n':
            print("\nThanks for playing!")
            break
            
        
getHello()

