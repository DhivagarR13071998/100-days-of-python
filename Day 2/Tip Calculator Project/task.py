print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")

# A restaurant applies a 10% discount on a $120.00 bill before tip. After the discount, the group of 4 wants to leave an 18% tip on the discounted amount. How much does each person pay?

print("Welcome to the restaurant tip calculator!")

discount_percent   = int(input("What is the discount percentage? "))
bill_before_tip    = float(input("What was the bill before discount? $"))
discount_rate      = discount_percent / 100

people             = int(input("How many people to split the bill? "))
tip_percent        = int(input(f"{people} people want to tip what percentage? "))
tip_rate           = tip_percent / 100

# 1. Apply discount
discounted_amount  = bill_before_tip * (1 - discount_rate)

# 2. Add tip
total_with_tip     = discounted_amount * (1 + tip_rate)

# 3. Split between people
per_person         = total_with_tip / people

# 4. Show result
print(f"Each person should pay: ${per_person:.2f}")

# Bill: $ eighty-seven fifty cents, split 3 ways, tip 18%

# (87.50 / 3) * 1.18 ≈ 34.4167
# → formatted to 2 dp → 34.42

Totalbill = float(input("What was the total bill? $"))
tip = int(input("Tip percent was "))
tip_after_percent = tip / 100
split = int(input("How many people? "))

# 1. Calculate the tip amount only
total_tip = Totalbill * tip_after_percent

# 2. Add the tip to the original bill
total_amount = Totalbill + total_tip

# 3. Divide by the number of people
Perperson = total_amount / split

print(f"Each person should pay: ${Perperson:.2f}")
