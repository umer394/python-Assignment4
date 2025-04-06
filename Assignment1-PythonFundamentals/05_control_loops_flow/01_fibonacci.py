def main():
    curr_num = 0
    next_num = 1
    user_num = int(input("Enter a number from where you want a fibbonacci series: "))
    while curr_num <= user_num:
        print(curr_num)
        term_after_next = curr_num + next_num
        curr_num = next_num
        next_num = term_after_next
if __name__ == '__main__':
    main()