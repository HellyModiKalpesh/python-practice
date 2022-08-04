#  18)WAP to print whether no. is Palindrome or not and reverse also
'''''
print("enter the number")
number= int(input())
temp= number
reverse= 0

while(number>0):
    dig = number%10
    reverse = reverse *10 +dig
    number = number//10
    
if temp ==reverse :
    print("it is an palindrome")
else:
    print("not a palindrome")
    
print("reversed number is",reverse)  '''  

#21) WAP to find sum of digit.
''''
print("enter the number")
n=int(input())
sum=0

while(n>0):
    dig=n%10
    sum=sum+dig
    n=n//10
    
print("sum is ",sum)'''

#22)WAP to find sum of odd digit of entered digit.

#WAP to print 1 to 100 (ascending ) & 100 to 1 (reverse ) using For loop 
'''
for i in range(1,101):
    print(i)'''
 
'''for i in range(100,0,-1):
     print(i)'''
     
 #   24)WAP to print no’s between no1. To no2.
 
 print("enter the number")
 a=int(input())
 print("enter the no2")
 b=int(input())
 
    while()