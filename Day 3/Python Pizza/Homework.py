# 🎬 Practice Project: Python Movie Booking
# Congratulations, you've got a job at Python Cinemas!
# Your first job is to build an automatic movie ticket billing system.

print("Welcome to Python Movie Booking!")
Age = int(input("Enter your age: "))
popcorn = input("Do you want popcorn? Y or N: ")
Glasses = input("Do you want 3D glasses? Y or N: ")

# Ticket price based on age
if Age < 12:
    price = 150
elif 12 <= Age <= 18:
    price = 200
else:
    price = 250

# Add-ons (available for all)
if popcorn == "Y":
    price += 50
if Glasses == "Y":
    price += 30

print(f"Your final ticket price is: ₹{price}.")
