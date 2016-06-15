import random
totalQuestions=10
result=0
correct=0
for i in range(0,totalQuestions):
	num1=random.randint(1,100)
	num2=random.randint(1,20)
	ops=random.randint(0,3)
	if ops==0:
		#addition
		print(str(num1)+"+"+str(num2)+"?")
		result=num1+num2
	elif ops==1:
		#subtraction
		print(str(num1)+"-"+str(num2)+"?")
		result=num1-num2
	elif ops==2:
		#multiplication
		print(str(num1)+"*"+str(num2)+"?")
		result=num1*num2
	elif ops==3:
		#division
		print(str(num1)+"/"+str(num2)+"?")
		result=num1//num2 #floor divison to keep as integer
	guess=input()
	if int(guess)==result:
		print('Well done!!')
		correct+=1
	else:
		print('Sorry!! The answer is'+str(result))
print('Your score: '+str(correct)+'correct and '+str(totalQuestions - correct)+'wrong')
if correct>7:
	print('Good job')
else:
	print('Try Again!! You can do a good job')
