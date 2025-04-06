def main():
    current_num = int(input("Enter a number you want to double it: "))
    while current_num < 100:
         print(f"{current_num} doubled is {current_num * 2}")
         current_num = current_num * 2

if __name__ == '__main__':
    main()