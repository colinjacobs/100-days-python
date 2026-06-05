import math
number_to_check = int(input("Enter the number\n"))
dividers = []
num_sqrt = int(math.sqrt(number_to_check))
if number_to_check < 2:
    print("Numbers less than 2 are not prime.")
elif number_to_check == 2:
    print("Number is prime")
#elif number_to_check % 2 == 0:
#    print("Number is even and therefore not prime")
else:
    for number in range(2,num_sqrt+1):
        if number_to_check % number == 0:
            dividers.append(number)
            dividers.append(int(number_to_check/number))
    if not dividers:
        print(f"{number_to_check} is prime.")
    else:
        unique_dividers = list(dict.fromkeys(dividers))
        print(f"{number_to_check} is not prime.\nDividers: {sorted(unique_dividers)}")
