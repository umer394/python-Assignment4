import random
def main():
    dice1:int = random.randint(1,6)
    dice2:int = random.randint(1,6)
    print("Dice Roll")
    print(f"First Dice : {dice1}")
    print(f"Second Dice : {dice2}")
    print(f"Total : {dice1 + dice2}")

if __name__ == '__main__':
    main()