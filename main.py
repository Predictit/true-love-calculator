
name1 = input("Name? ").lower()
name2 = input("Second name? ").lower()
total = 0


if name1.count('t') > 0:
    total +=10
if name1.count('r') > 0:
    total += 10
if name1.count('u') > 0:
    total += 10
if name1.count('e') > 0:
    total += 10

if name2.count('t') > 0:
    total +=10
if name2.count('r') > 0:
    total += 10
if name2.count('u') > 0:
    total += 10
if name2.count('e') > 0:
    total += 10

if name1.count('l') > 0:
    total +=1
if name1.count('o') > 0:
    total += 1
if name1.count('v') > 0:
    total += 1
if name1.count('e') > 0:
    total += 1

if name2.count('l') > 0:
    total +=1
if name2.count('o') > 0:
    total += 1
if name2.count('v') > 0:
    total += 1
if name2.count('e') > 0:
    total += 1

love_score = total
print(f"Your score is {love_score}.")

if 10 < love_score > 90:
    print(f"Your score is {love_score} you go together like coke and mentos")
if 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")