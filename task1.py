from math import floor
from operator import floordiv
from re import I
from tempfile import tempdir


'''a=10
b=20
c=30
sum=a+b+c
print("sum of a number is",sum)
avg=a+b+c/3
print("average is",avg)'''

#converting into minutes
'''print("enter the no")
s=int(input())
print("no is",s)
m=s/60
print("min is ", m)
h=s/3600
print("hour is ",h)'''
#area of a different shape

'''print("enter the L")
L=int(input())
print("enter the b")
b=int(input())
print("enter the radius")
r=int(input())
aor=L*b
print("area of a rectangleis",aor)
print("area of a square",L*L)
print("area of a circle",3.14*r*r)'''
#simple interest

'''print("enter the principle amount")
p=int(input())
print("enter the rate of interest")
rate=int(input())
print("enter the time of interest")
n=int(input())
Interest=(p*rate*n)/100
print("simple interest is",Interest)'''
#)WAP to Get no. of Days as inputs and find out Months, Year and Remaining Days
'''
print("enter the user days")
user_days=int(input())
year=user_days//365
month=user_days//30
week=(user_days%365)//7     # here we use floor division to get first values
rem_days=(user_days%365)%7 # lets assume days=768 then rem days = 768%365=38 days then 38%7(week)=3 days remaining
print("year is",year)
print("months is",month)
print("week is",week)
print("remaining days",rem_days)'''

#)WAP to Interchange or Swap numbers using third variable
'''a=10
b=5
temp=a
a=b
b=temp
print("value of a a",a)
print("value of a b",b)'''

#WAP to find out whether given no. is odd or even
'''print("enter the no")
n=int(input())
if n%2==0:
    print("no is even")
else:
    print("no is odd")'''

#8) WAP to find out whether given no. is positive or negative
'''
print("enter the no")
n=int(input())
if n<0:
    print("no is negative")
else:
    print("no is positive")'''
    
#9)WAP to find out maximum
'''
print("enter the no1")
a=int(input())
print("enter the no2")
b=int(input()) 
if a>b:
    print("a is max")
else:
    print("b is max")''' 
   
   # find out the max among 3 numbers
'''a=10
b=12
c=11
if(a>b)and(a>c):
    print("a is max")
elif(b>a)and(b>c):
    print("b is max") 
else:
    print("c is max")'''
#10) WAP to find out grade from inputted marks.

'''print("enter the marks")
n=int(input())
if n>90:
    print("grade A")
elif n>80:
    print("grade B")
elif n>60:
    print("grade C")
elif n>50:
    print("garde D")
else:
    print("fail") '''
#11)Write a menu driven program to perform arithmetic operations Using If-else  

'''print("enter the no1")
x=int(input())
print("enter the no2")
y=int(input())
print("enter your choice")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
n=int(input("enter your choice""(1-4)"))
if n==1:
    print("add is",(x+y))
elif n==2 :
    print("subtraction is",(x-y))
elif n==3:
    print("multiplication is",(x*y))
elif n==4:
    print("division is",(x/y))
else:
    print("please select the correct choice")'''

#WAP to check whether entered no. in between 1-5 , 6-10 or greater than 10.    
'''print("enter the no")
n=int(input())
if n in range(1,6):
    print("no is in the (1-5)")
elif n in range(6,11):
    print("no is in the (6-10)")
elif n>10:
    print("n is greater than 10")
else:
    print("no is greater or negative") '''

#13)WAP Program to print 1 to 10.
'''for i in range(1,11):
    print(i)'''
 
#    WAP Program sum of 1 to 10.
'''sum=0
for i in range(1,11):
    sum+=i
print("sum",sum)'''  

#15)WAP to find power of a given number
'''print("enter the no")
n=int(input())
x=pow(n,3)
print("power is ",x)'''

#16)WAP to find factorial of a given number

print("enter the no")
n=int(input())
factorial=1

if n==0:
    print("factorial is 1")
else:
       for i in range(1,n+1):
            factorial=factorial*i
            
print("factorial is ", factorial)

#17)WAP check the no. Armstrong or not

'''n=int(input("enter the number"))
sum=0
order= len(str(n))
temp=n
while(n>0):
    digit= n%10 
    sum += digit**order
    n=n//10
if(sum == temp):
    print("it is an armstrong number")
else:
    print("not an armstrong")'''
    
