

# Declare a function with 3 arguments....
def readint(prompt, min, max):
    check = False
    while not check:
        # Use try except methods to handle errors....
        try:
            num = int(input(prompt))
            check = True
        except ValueError:
            print("Error: wrong input")
        if check:
            check = num >= min and num <= max
        if not check:
            print(
                f"Error: the num is not within permitted range from {min} to {max}")
    return num
    
v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
