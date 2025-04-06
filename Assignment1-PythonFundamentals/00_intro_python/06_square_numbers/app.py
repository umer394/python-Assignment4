def main():
    try:
        num: float = float(input("Type a number to see its square: "))
        print(str(num) + " squared is " + str(num ** 2)) 
    except:
        print("Enter number only")
        main()

if __name__ == '__main__':
    main()