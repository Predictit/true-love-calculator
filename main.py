
name1 = input("Name? ")
name2 = input("Second name? ")
total = 0

combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

print(f"Your score is {score}.")

if 10 < score > 90:
    print(f"Your score is {score} you go together like coke and mentos")
if 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")