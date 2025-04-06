def main():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    user_fruit = str(input("Enter a fruit to add in a list:"))
    if user_fruit in fruit_list:
        print(f"{user_fruit} is already in the list: {fruit_list}")
    else:
        fruit_list.append(user_fruit)
        print(fruit_list)
if __name__ == '__main__':
    main()