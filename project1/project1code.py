# The goal of my project is for users to guess if a number is higher or lower.
# A log will be kept based on how many guess they get in a row
import time, random

print('Please enter your initials: ')
usrName = input()


# A username (the initials) will be kept for each score

# Creating a prompt for the user, outlining the basic rules.
print('Welcome to Higher or Lower! How long can you keep guessing?')
time.sleep(1)
print('The goal of the game is to guess whether the new number is higher or lower than the last.')
time.sleep(1)
print('You think you can keep up? Let\'s find out!')
time.sleep(1)
print('The range of number\'s is between 1 and 10. Good luck!')
time.sleep(2)

newNum = random.choice(range(1, 11))
guessTot = 0
gameOver = 0

while(gameOver != 1):
    oldNum = newNum
    newNum = random.choice(range(1, 11))
    
    print('Is the new number higher or lower than ' + str(oldNum) + '? (Please type \'Higher\' or \'Lower\')')
    myGuess = input()

    if newNum < oldNum and myGuess == 'Lower' or newNum < oldNum and myGuess == 'lower':

        print('Correct! The number was ' + str(newNum) + ', which is lower!')
        guessTot = guessTot + 1


    elif newNum > oldNum and myGuess == 'Higher' or newNum > oldNum and myGuess == 'higher':
        
        print('Correct! The number was ' + str(newNum) + ', whcih is higher!')
        guessTot = guessTot + 1


    ### Wanted to test with throwing an error with an incorrect input, but did not have the time to figure it out.
    #elif myGuess != 'Higher' or myGuess != 'higher' or myGuess != 'Lower' or myGuess != 'lower':

        #print('Please select a valid response!')


    else:
        gameOver = 1

### If I had more time, I would have output the final score to another text document.        
print('Sorry! You guessed incorrectly. ' + str(usrName) + ' finished the game with ' + str(guessTot) + ' correct guess(es)!')
        
