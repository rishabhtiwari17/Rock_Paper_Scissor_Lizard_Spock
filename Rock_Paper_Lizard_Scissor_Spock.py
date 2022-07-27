import random


def gameWin(comp, you):
    if (comp == you):
        return None
    elif comp == 'rock':
        if you == 'paper':
            return True
        elif you == 'spock':
            return True
        else:
            return False
    elif comp == 'paper':
        if you == 'scissor':
            return True
        elif you == 'lizard':
            return True
        else:
            return False
    elif comp == 'scissor':
        if you == 'paper':
            return False
        elif you == 'lizard':
            return False
        else:
            return True
    elif comp == 'lizard':
        if you == 'scissor':
            return True
        elif you == 'rock':
            return True
        else:
            return False
    elif comp == 'spock':
        if you == 'lizard':
            return True
        elif you == 'paper':
            return True
        else:
            return False


print("comp turn  he is choosing stone, paper,scissor,lizard,spock.")
randno = random.randint(1, 6)
if randno == 1:
    comp = 'rock'
elif randno == 2:
    comp = 'paper'
elif randno == 3:
    comp = 'scissor'
elif randno == 4:
    comp = 'lizard'
elif randno == 5:
    comp = 'spock'
choices = ["rock", "paper", "scissor", "lizard", "spock"]
you = input("Enter your choice(rock,paper,scissor,lizard,spock)\n")
if you in choices:
    a = gameWin(comp, you)
    print(f"comp chose {comp}")
    print(f"you chose {you}")
else:
    print("Select From choices")

if a == None:
    print("boo u are tied")
elif a:
    print("You win bro")
else:
    print("You lose bro")
