# Reverse Guessing Game in Python
# You think of a number - Computer guesses it
print ('Hey there!! What is your name?')
myName=input()
print('Well hello!!'+myName)
print('Please think of a number between 1-100. I will guess it')
low=1
high=100
mid=0
while low<high:
	mid=(low+high)//2
	print('Is the number'+str(mid))
	response=input()
	if response=='L':
		high=mid-1
	if response=='H':
		low=mid+1
	if response=="Y":
		break;

if low==high:
	print('Your number is:'+str(low))

print('Great game'+myName)