def main():
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))
    if(divisor==0):
        print("Divisor must be greater than zero")
        main()
    else:
        quotient: int = dividend // divisor  
        remainder: int = dividend % divisor  
        print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))


if __name__ == '__main__':
    main()