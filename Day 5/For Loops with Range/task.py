#Range function only works with loop
# it always works with -1 in the last

#a <= range(a, b) < b
# total = 0
# for number in range(1,101):
#     total += number
# print(total)


for number in range(1,101):
    if number % 3 ==0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 ==0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
