import random

NUM_ROUNDS = 5

def main():
    SCORE : int =  0
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    for i in range(1,6):
        print(f"Round {i}")
        computer_num = random.randint(1,100)
        user_num = int(input("Your Number is: "))
        user_guess = input("Do you think your number is higher or lower than the computer's?: ")
        if user_num > computer_num and user_guess.lower() == "higher":
            SCORE += 1
            print(f"You were right! The computer's number was {computer_num}")
            print(f"Your score is now {SCORE}")
        elif user_num < computer_num and user_guess.lower() == "lower":
            SCORE += 1
            print(f"You were right! The computer's number was {computer_num}")
            print(f"Your score is now {SCORE}")
        elif user_num < computer_num and user_guess.lower() == "higher":
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")
            print(f"Your score is now {SCORE}")
        elif user_num > computer_num and user_guess.lower() == "lower":
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")
            print(f"Your score is now {SCORE}")
    
    if(SCORE == 5):
        print("Wow! You played perfectly")
    elif(SCORE >2 and SCORE < 5):
        print("You won at least half the rounds")
    else:
        print("Better luck next time!")

    print("Thanks for Playing!")
    

if __name__ == "__main__":
    main()