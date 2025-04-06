def main():
    numbers_list : int = [2,4,6,8]
    for i in range(len(numbers_list)):
        element = numbers_list[i]
        numbers_list[i] = element * 2 
    print(f"The Double of  list is {numbers_list}")
if __name__ == '__main__':
    main()