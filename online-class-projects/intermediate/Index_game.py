def access(current_list):
    element_index = int(input(f"Enter a index you want to access: "))
    try:
        return current_list[element_index]
    except:
        return f"Index {element_index} is out of range"

def modify(current_list):
    element_index = int(input(f"Enter a index you want to modify: "))
    new_value = str(input(f"Enter a value you want to modify at index {element_index}: "))
    try:
        current_list[element_index] = new_value
        return current_list
    except:
        return f"Index {element_index} is out of range"
def slicing(current_list):
    start = int(input("Enter start index: "))
    end = int(input("Enter end index: "))
    try:
        return current_list[start:end]
    except:
        return "Invalid indices."
def main():
    print("Welcome to Index Game")
    print("-----------------------")
    list_of_elements = ["apple","pakistan","currency","parrot","ball"] 
    print(f"We have a list to access,modify and slicing {list_of_elements}")
    operation = str(input("Select an operation:(access,modify,slicing) "))
    if(operation.lower() == "access"):
        print(access(list_of_elements))
    elif(operation.lower() == "modify"):
        print(modify(list_of_elements))
    elif(operation.lower() == "slicing"):
        print(slicing(list_of_elements))
    else:
        print("Select in above options only")
    
if __name__ == '__main__':
    main()