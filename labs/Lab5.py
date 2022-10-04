# The problem I selected is guessing a random number, but I added some twists!
import time, random

print('Choose a level of difficulty ("Noob", "Intermediate", "Hard")')
selDiff = input()

# I set myNum to -1 to keep the while loop going until a correct level is picked.
# The myNum doesn't change it's value until one of three levels is entered.
myNum = -1

while myNum == -1:
    if selDiff == 'Noob' or selDiff == 'noob':

        print('You have selected "Noob" difficulty! Smart choice.')
        time.sleep(1)

        myNum = random.choice(range(1, 11))
        giveRng = '1 and 10.'


    elif selDiff == 'Intermediate' or selDiff == 'intermediate':

        print('You have selected "Intermediate" difficulty! You may regret this...')
        time.sleep(1)

        myNum = random.choice(range(1, 51))
        giveRng = '1 and 50.'


    elif selDiff == 'Hard' or selDiff == 'hard':

        print('You have selected "Hard" difficulty! There\'s no turning back now!')
        time.sleep(1)

        myNum = random.choice(range(1, 101))
        giveRng = '1 and 100.'


    else:
        print('Please carefully select one of the available options!')
        selDiff = input()


# The system has picked a number based on the selected difficulty
print('I am thinking of a number between ' + giveRng)
time.sleep(5)

print('I\'ve got it! What number am I thinking of?')
numGuess = input()

# Keeps running until the correct number is guessed.
while numGuess != int(myNum):
    try:
        numGuess = int(numGuess)
        if numGuess < int(myNum):
            print('Nope! My number is higher. Guess again!')
            numGuess = int(input())
            
        elif numGuess > int(myNum):
            print('Woah, that\'s too high! Guess again!')
            numGuess = int(input())

# This dialogue comes up when you enter something that is not an Integer.
    except ValueError:
            print('You got it!')
            time.sleep(2)
            print('Just kidding. Do you see how no one is laughing? Guess again!')
            print('(This time, make it a number.)')
            numGuess = int(input())

# Final dialogue when the user guesses correctly
print('Congratulations! You correctly guessed my number, which was %s.' % myNum)




    
