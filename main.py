import random

def game(a,b):
    if a == b:
        return None
    elif a == 'r':
        if b == 's':
            return False
        elif b == 'p':
            return True
    elif a == 'p':
        if b == 'r':
            return False
        elif b == 's':
            return True
    elif a == 's':
        if b == 'p':
            return False
        elif b == "r":
            return True

print("Computer's turn : Rock(r) Paper(p) or Scissors(s)?")
d = random.randint(1,3)
if d==1:
    a = 'r'
elif d==2:
    a = 'p'
elif d==3:
    a = 's'

b = input("Your turn : Rock(r) Paper(p) or Scissors(s)?")
c = game(a,b)

print(f"Computer chose {a}")
print(f"You chose {b}")

if c == None:
    print("The game is a tie!")
elif c:
    print("You Win!")
else:
    print("You Lose!")