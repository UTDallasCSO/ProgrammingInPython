# Guess the number game using Python
# Can you guess the number in the Computer's mind??
import random 

guessesDone = 0

print("Hello!! What's your name?")

myName=input()

number=random.randint(1,100)
print('Well,'+ myName + ', I am thinking of a number between 1 and 100.')
print('Can you guess it?')

while guessesDone < 6:
    print('Take a guess:')
    guess=input()
    guess=int(guess)
    
    guessesDone = guessesDone + 1
    
    if guess< number:
        print('Your guess is too low.')
    
    if guess > number:
    	print('Your guess is too high.')
    
    if guess == number:
    	break
    

if guess == number:
	guessesDone = str(guessesDone)
	print('Good job!!'+ myName + ' You guessed it in' + guessesDone + 'guesses')

if guess!=number:
	number=str(number)
	print('Sorry you are out of tries. I thought of' + number)
 