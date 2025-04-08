import random

def guess_num(x):
    print("Guess My Number")
    print(f"I am thinking of a number between 0 and {x}... ")
    my_num = random.randint(1,x)
    return my_num

# def computer_guess(x):
#     low = 1
#     high = x
#     feedback = ''
#     while feedback != 'c':
#         if low != high:
#             guess = random.randint(low, high)
#         else:
#             guess = low  
#         feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
#         if feedback == 'h':
#             high = guess - 1
#         elif feedback == 'l':
#             low = guess + 1
#     print(f"Yay! The computer guessed your number {guess} correctly!")
def main():
    my_num = guess_num(10)
    while True:
        user_guess = int(input("Enter a Guess:"))
        if(user_guess > my_num):
            print("Your Guess is to high")
        elif(user_guess < my_num):
            print("Your Guess is to low")
        elif(user_guess == my_num):
            print(f"Congrats! The number was: {user_guess}")
            break
    # computer_guess(10)
if __name__ == '__main__':
    main()