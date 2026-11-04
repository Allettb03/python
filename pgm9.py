num1=int(input ("enter first number"))
num2=int(input ("enter first number"))
num3=int(input ("enter first number"))

if (num1>num2) and (num1>num3):
  f = num1
elif(num2>num3):
  f = num2
else:
  f = num3
print("the largest number is",f)  
     
