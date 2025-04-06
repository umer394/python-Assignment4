import time
def main():
    for i in range(10):
        time.sleep(1)
        print(10 - i)
    time.sleep(1)
    print("Lift Off!")
if __name__ == '__main__':
    main()