import random
x = 0
y = 0
v = True
while (x < 1):
    y += 1
    if v == True:
        secret_number = random.randint(1, 10)
        guess = int(raw_input("I am thinking of a number between 1 and 10. \nWhat's the number? "))
        v = False
    if secret_number == guess:
        print "Yes you win!"
        v = True
        bonus = raw_input("Would you like to play again?! (yes or no)")
        if bonus == "yes":
            y = 0
        else:
            print "Bye!!"
            x += 1

    elif y == 5:
        print "You ran out of guesses, and you lose!!"
        x += 1

    elif guess < secret_number:
        print "%d is too low." % guess
    else:
        print "%d is too high." % guess

    if (v == False):
        print "You have %d guesses left." % (5 - y)
        guess = int(raw_input("What's the number? "))
