import random

def guess_choice():
    thislist = ["rock", "paper", "scissors"]
    user_points = 0
    computer_points = 0
    rounds_number = 0
    #print("rock", "paper", "scissors")
    #choices = ["rock", "paper", "scissors"]
    print("Choose your option")
    computer = random.choice(thislist)
    
    while rounds_number < 3:
        user_option = str(input())
        rounds_number  += 1
        if user_option == "rock" and computer == "paper":
            computer_points += 1
            print("Computer point")
        elif user_option == "paper" and computer == "rock":
            user_points +=1
            print("Your point") 
        elif user_option == "scissors" and computer == "paper":
            user_points +=1
            print("Your point")
        elif user_option == "paper" and computer == "scissors":
            computer_points +=1
            print("Computer pont")
        elif user_option == "scissors" and computer == "rock":
            computer_points +=1
            print("Computer point")
        elif user_option == "rock" and computer == "scissors":
            user_points +=1
            print("Your point")
        elif user_option == computer:
            print("Let's try again")

    if user_points > computer_points:
        print("User win")
    else:
        print("Computer win")



if __name__ == "__main__":
    next_game = True
    while next_game:
        guess_choice()
        next_time_input = input("Do you want to play next time? y/n")
        if next_time_input == 'n':
            next_game = False 


    








