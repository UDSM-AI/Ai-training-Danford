def armstrong_number(number):
    num_str = str(number)
    n = len(num_str)
    armstrong_number_sum = sum(int(digit)**n for digit in num_str)
    if armstrong_number_sum == number:
        return True
    else:
        return False
#number = 123
number = int(input("Enter the number you need to test if it is armstrong: "))
if armstrong_number(number):
    print(f"{number} is armstrong number")
else:
    print(f"{number} is not armstrong number")