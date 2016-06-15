print('Enter the day of the week') #0-6 Monday to Sunday
day=input()
dayOfWeek=int(day)
while dayOfWeek<5:
	print('No, there is school tomorrow!! You cannot play')
	dayOfWeek+=1
print("Today is a weekend!! You can play today ")