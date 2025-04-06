def main():
    BOLD_ITALIC = "\033[1;3m"
    RESET = "\033[0m"
    animal = input("What's your favorite animal? ")
    print(f"My favorite animal is also {BOLD_ITALIC}{animal }{RESET}")
if __name__ == '__main__':
    main()