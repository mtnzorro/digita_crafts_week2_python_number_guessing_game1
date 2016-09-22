import random
secret_number = random.randint(1, 10)
guess = int(raw_input("I am thinking of a number between 1 and 10. \nWhat's the number? "))
x = 0
y = 0
while (x < 1):
    y += 1
    if secret_number == guess:
        print "Yes you win!"
        bonus = raw_input("Would you like to play again?! (yes or no)")
        if bonus == "yes":
            y = 0

            secret_number = random.randint(1, 10)
            guess = int(raw_input("I am thinking of a number between 1 and 10. \nWhat's the number? "))

        else:
            print "Bye!!"
            x += 1

    elif y == 5:
            print "You ran out of guesses, and you lose!!"
            x += 1
    elif guess < secret_number:
        print "%d is too low." % guess
        print "You have %d guesses left." % (5-y)
        guess = int(raw_input("What's the number? "))

    else:
        print "%d is too high." % guess
        print "You have %d guesses left." % (5 - y)
        guess = int(raw_input("What's the number? "))
