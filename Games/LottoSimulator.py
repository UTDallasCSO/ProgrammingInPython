#Program to simulate the Texas Lotto
#We will simulate random generation of 6 numbers without duplicates

import random
import time
list=[]
for i in range(0,6):
	while True:
		num=random.randint(1,50)
		list.append(num)
		dups=False
		for j in range(0,i):
			if list[i]==list[j]:
				dups=True
				print('Dups found:'+str(list[i]))
		if dups==True:
			break;
	print('Item:'+str(i+1)+':'+list[i])
	time.sleep(2)


