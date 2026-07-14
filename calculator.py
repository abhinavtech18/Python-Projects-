print("""Hello welcome to Abhinav's Special Calculator

we work on following operations: 
1. Addition
2. Substraction
3. Multiplication
4. Division
5. Exit""")
a= int(input("enter the serial number of operation that you want to perform: "))
if a>1 or a<5:
	while a!=0:
		num1= int(input("enter your first number: "))
		num2= int(input("enter your second number: "))
		if (a==1):
			print("your result is : ", num1+num2)
		elif (a==2):
			print("your result is:  ", (num1-num2))
		elif (a==3):
			print("your result is:  ", num1*num2)
		elif(a==4):
			if num2!=0:
				print("Your Denominator cant be 0")
			else:
				print(num1/num2)
	else:
			print("THANKYOU!!!!")
			
else:
		print("Please write valid number from 1 to 5")
				