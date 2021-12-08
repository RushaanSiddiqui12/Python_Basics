import random

def game(comp, you):
    if(comp == you):
        return None
    elif(comp == 'r'):
        if(you == 's'):
            return False
        elif(you == 'p'):
            return True
    elif(comp == 'p'):
        if(you == 's'):
            return True
        elif(you == 'r'):
            return False
    elif(comp == 's'):
        if(you == 'r'):
            return True
        elif(you == 'p'):
            return False
    
print("Computer Turn: Rock(r), Paper(p) or Scissors(s) ")
rand_num = random.randint(1, 3)
if (rand_num == 1):
    comp = 'r'
elif (rand_num == 2):
    comp = 'p'
elif (rand_num == 3):
    comp = 's'

you = input("Your Turn: Enter Rock(r), Paper(p) or Scissors(s) = ")
a = game(comp, you)

print("Computer chose = ", comp)
print("You chose = ", you)

if (a == None):
    print("******The Game is a tie. Thankyou for playing.******")
elif (a):
    print("******You Win******")
else:
    print("******You Lose******")
