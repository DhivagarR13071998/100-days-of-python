print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm:\n "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age:\n"))
    if age <= 12:
        print("Please pay $5 and Enjoy your ride.")
    elif age <= 18:
        print("please pay $7 and Enjoy your ride.")
    else:
        print("please pay $12 and Enjoy your ride.")
else:
    print("Sorry you have to grow taller before you can ride.")
