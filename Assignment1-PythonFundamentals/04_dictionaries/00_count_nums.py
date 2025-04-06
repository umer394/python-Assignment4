def get_user_nums():
    user_nums = []
    while True:
        user = input("Enter a number : ")

        if (user == ""):
            break
        else:
            user_nums.append(int(user))
    return user_nums

def count_nums(num_list):
    num_dict = {}
    for num in num_list:
        if num not in num_dict:
            num_dict[num]=1
        else:
            num_dict[num] += 1
    return num_dict

def print_counts(num_dict):
    for num in num_dict:
        print(f'{str(num)} appears {num_dict[num]} times')
def main():
    user_numbers = get_user_nums()
    num_list = count_nums(user_numbers)
    print_counts(num_list)
    
if __name__ == '__main__':
    main()

