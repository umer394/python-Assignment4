import random

def guess_num():
    print("Guess My Number")
    print("I am thinking of a number between 0 and 99... ")
    my_num = random.randint(1,99)
    return my_num
def main():
    my_num = guess_num()
    while True:
        user_guess = int(input("Enter a Guess:"))
        if(user_guess > my_num):
            print("Your Guess is to high")
        elif(user_guess < my_num):
            print("Your Guess is to low")
        elif(user_guess == my_num):
            print(f"Congrats! The number was: {user_guess}")
            break
if __name__ == '__main__':
    main()