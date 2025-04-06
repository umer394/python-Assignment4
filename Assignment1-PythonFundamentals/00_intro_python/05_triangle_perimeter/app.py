def main():
    try:
        first_side = float(input("What is the length of side 1? "))
        second_side = float(input("What is the length of side 2? "))
        third_side = float(input("What is the length of side 3? "))
        print("The perimeter of the triangle is " + str(first_side + second_side + third_side))
    except Exception:
        print("Length must be in numbers")
        main()

if __name__ == '__main__':
    main()