# bmi = 84 / 1.65 ** 2
height = 1.65
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
#BMI = weight (kg) / (height (m))²
bmi =weight / height ** 2

print(int(bmi))
print(round(bmi)) # used to rouund of the value like 30.89 to 31
print(round (bmi,2)) # used to round the number after two digits like 30.851212121 to 30.85

#Assignment Operators
# Assignment operators such as the addition assignment operator += will add the number on the right to the original value of the variable on the left and assign the new value to the variable.
#
# +=
#
# -=
#
# *=
#
# /=
score = 0
score +=1
print(score)
score -=1
print(score)
score *=2
print(score)
score /=1
print(score)

age = 12

print(f"I am {age} years old") # using f" and {value of the int} that needs to be printed

Score = 12
print(f"My team score is {Score}")

Score = 12
height = 1.8
is_Winning = True

print(f"The height:{height} and score: {Score} of the team leads to is winning into {is_Winning}")