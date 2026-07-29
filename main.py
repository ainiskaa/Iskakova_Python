# Test task


def check_number():
    number = int(input("Enter a number: "))
    if number > 7:
        print ("Hello")

def check_name():
    name = input("Enter a name: ")
    if name.lower() == "john":
        print ("Hello, John")
    else:
        print ("There is no such name")

def print_numbers_divisible_by_three():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Numbers divisible by 3:")
    found = False
    for number in numbers:
        if number % 3 == 0:
            print(number)
            found = True
    if not found:
        print("There are no numbers divisible by 3.")


def main ():
    check_number()
    check_name()
    print_numbers_divisible_by_three()

if __name__ == "__main__":
    main()