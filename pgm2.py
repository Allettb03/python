
list1=[11,-27,45,66,-93]
for num in list1:
  if num>=0:
   print(num,end="")
     
     
  
   print("Enter the limit:")
   n=int(input())
   squares=[i*i for i in range (n)]
   print("square of n numbers \n",squares)   
   
   
   
   word=input('Enteryour word:')
   for letter in word:
    if letter in ('aeiou'):
     print(letter,end='')  
     
     
     list1=['aravind','aparna']
     print("The orginal list:\n"+str(list1))
     res=[ord(ele)for sub in list1 for ele in sub]
     print("The ASCII list is :\n"+str(res))
     
