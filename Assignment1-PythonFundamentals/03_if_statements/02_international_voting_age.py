def main():
    peturksbouipo_age : int = 16
    stanlau_age : int = 25
    mayengua_age  : int = 48
    user_age = int(input("How old are you?"))
    if(user_age >= peturksbouipo_age):
        print("You can vote in Peturksbouipo where the voting age is " + str(peturksbouipo_age) + ".")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is " + str(peturksbouipo_age) + ".")
    
    
    if user_age >= stanlau_age:
        print("You can vote in Stanlau where the voting age is " + str(stanlau_age) + ".")
    else:
        print("You cannot vote in Stanlau where the voting age is " + str(stanlau_age) + ".")
    
    
    if user_age >= mayengua_age :
        print("You can vote in Mayengua where the voting age is " + str(mayengua_age ) + ".")
    else:
        print("You cannot vote in Mayengua where the voting age is " + str(mayengua_age ) + ".")
        
if __name__ == '__main__':
    main()