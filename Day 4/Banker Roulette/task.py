import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st Option
print(random.choice(friends))

# 2nd Option
random_index = random.randint(0, 4)
print(friends[random_index])


Names = ["Ragul", "Dhivagar",'Ravi', 'Sasi']
print(random.choice(Names))

random_index2 = random.randint(0,4)

print(Names[random_index2])