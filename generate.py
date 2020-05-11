from random import randint


def generate_number(startNumber, LastNumber):
    random_stack = []
    occurance = 0
    while True:
        value = randint(startNumber,LastNumber)
        if value in random_stack:
            print("found occurance "+ str(value))
            break;
        else:
            random_stack.append(value)
            
    print(random_stack)
    
    


first = int(input("Enter minimum number"))
last = int(input("Enter maximum number"))
generate_number(first,last)
# loop_number = int(input("Enter occurance of same number (default is 2)"))

# loop_number = Check_number(loop_number)

# def Check_number(loop_number):
#     if loop_number > 10:
#     print("Keep occurance of same number less than 10. Else loading time will be more")
#     loop_number = int(input("Enter occurance of same number (default is 2)"))
    
