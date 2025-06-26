# Ask the user for their name.
your_name = input("Enter your name: ")
# Ask for their partner's name.
partners_name = input("Enter your partner's name:")

# Combine both names and convert to lowercase.
combined_names = your_name + partners_name
combined_names = combined_names.lower()
# Count how many times the letters in "TRUE" appear in the combined names.
t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e = combined_names.count('e')
# Count how many times the letters in "LOVE" appear in the combined names.
l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')
e2 = combined_names.count('e')
# Combine the counts to form a score.
true_score = t + r + u + e
love_score = l + o + v + e2
# Print a result based on the score:
final_score = int(str(true_score) + str(love_score))

if final_score < 10 or final_score>90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")

elif final_score > 40 or final_score <50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}")