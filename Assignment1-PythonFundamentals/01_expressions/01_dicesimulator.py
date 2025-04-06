import random



def roll_dice():
    dice1 : int = random.randint(1,6)
    dice2 : int = random.randint(1,6)
    print(f"Dice Roll : {dice1} , {dice2}")
    

def main():
    print("First Time Dice Roll")
    roll_dice()
    print("Second Time Dice Roll")
    roll_dice()
    print("Third Time Dice Roll")
    roll_dice()



if __name__ == '__main__':
    main()