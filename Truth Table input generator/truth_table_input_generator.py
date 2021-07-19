from os import system as sys

sys("title \"Truth Table Input Generator - Code by XENONZi - 10/28/2020\"")
sys("color a")

print("Code by XENONZi - 10/28/2020")
print("Enter 0 to exit")
print("Enter -1 to clear\n")

while 1:
    try:
        number_of_input = int(input("\nHow many inputs: "))
        if number_of_input == 0:
            break;
        elif number_of_input < 0:
            sys("cls")
            continue

        possible = (2**number_of_input)

        print("You have {} possible inputs".format(possible))
        print("All possible inputs:" )

        for i in range(possible):
            binary = str(bin(i)).replace("0b","")
            num_zero = number_of_input - len(binary);
            if num_zero != 0:
                binary = "0"*num_zero + binary
            print(binary)
    except Exception as e:
        print("Must be a number of type integer")


