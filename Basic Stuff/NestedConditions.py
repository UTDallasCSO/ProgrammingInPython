permission="No"
homeworkDone=True
if permission=="Yes" and ~homeworkDone:
	print("Complete your homework before that")
elif permission=="Yes" and homeworkDone:
	print("Go ahead!!")
elif permission=="No" and ~homeworkDone:
	print("No!! You can have smoothie instead")