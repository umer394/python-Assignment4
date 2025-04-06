def main():
    BOLD_ITALIC = "\033[1;3m"
    RESET = "\033[0m"
    try:
        user_input = float(input("Enter temperature in Fahrenheit: "))
        degrees_celsius = (user_input - 32) * 5.0/9.0
        print(f"Temperature {BOLD_ITALIC}{user_input}{RESET}F = {degrees_celsius}C")
    except Exception :
        print("Only numbers is accepted")
        main()
if __name__ == '__main__':
    main()