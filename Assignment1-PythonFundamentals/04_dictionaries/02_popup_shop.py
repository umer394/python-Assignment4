def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    total_costs = 0
    for fruit in fruits:
        user = int(input(f"How many {fruit} do you want?: "))
        # if user == 0:
        #     continue
        total_costs += user * fruits[fruit]
    print(f"Your total is ${total_costs}")

if __name__ == '__main__':
    main()