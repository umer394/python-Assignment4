

def main():
    lst = []
    user: str = input("Enter your number or press enter to stop : ")
    while user != "":
        lst.append(user)
        user: str = input("Enter your number or press enter to stop : ")
    if(len(lst) > 0):
        print(f"Here's The list : {lst}")
   
    else:
        print("enter something")
        main()
if __name__ == '__main__':
    main()
