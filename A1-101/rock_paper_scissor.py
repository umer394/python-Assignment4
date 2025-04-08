import random

def is_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return True

def main():
    user = input("What\'s your choice? 'r' for rock, 'p' for paper, 's' for scissors:\n ").lower()
    computer  = random.choice(['r', 'p', 's'])
    print(f"Computer\'s choice: {computer}")
    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You won!"
    return "You lost!"    
    
if __name__ == '__main__':
    print(main())