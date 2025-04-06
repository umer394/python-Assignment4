def first_element(lst):
    print(f"The last element of given list : {lst[-1]}")

def main():
    lst = []
    user: str = input("Enter your number or press enter to stop : ")
    while user != "":
        lst.append(user)
        user: str = input("Enter your number or press enter to stop : ")
    if(len(lst) > 0):
        print(f"The list : {lst}")
        first_element(lst)
    else:
        print("enter something")
        main()
if __name__ == '__main__':
    main()
