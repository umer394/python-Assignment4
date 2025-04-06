def main():
    try:
        first = int(input("Enter your frist number:"))
        second = int(input("Enter your second number:"))
        add = first + second
        print(f"The sum of {first} and {second} is : {add}")
    except  Exception as e:
        print("Only numbers is accepted")
        main()


if __name__ == '__main__':
    main()