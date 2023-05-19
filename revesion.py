
              #COMPLETE PYTHON

# REVISION PYTHON


#OPERRATORS


#arithmatic operator
"""
a=10
b=5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)
"""
#comparision operator
"""
a,b=10,20

print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)
print(a<b)
print(a>b)
"""
#assignment operator
"""
a=10
a+=10  a=a+10
a-=10  a=a-10
a/=10
a*=10
a%=10
"""
#logical operator
"""
a=10
b=20
print(a and b)
print(a or b)
print(not a)
"""
#bitwise operator
"""
and
or
xor
ones compliment
right side
left side
"""
#member ship operator
"""
print("a" in "vijay")
print("k" not in "vijay")
"""
#identify operator   memory place
"""
a=10
b=20
c=b
print(a is c)
print(b is b)
"""
# mutable and immutable

#mutable

#list
"""
a=[1,2,3,4,5,'a','v']
a[0]=2
print(a)
a[5]='b'
print(a)
"""
# dictionary
"""
a={
   "name":"kholi","rollno":2001,"age":21
    }
print(a)
a["name"]="jeeva"
print(a)
a["rollno"]=3001
print(a)
"""
# immutable

#string
"""
a="kholi vox"
a[1]="j"
print(a) #error
"""
#tuple
"""
a=(1,2,3,4,"d","f")
a[0]=2
print(a) #error
"""
#set
"""
a={1,2,3,4,5,"g","h"}
a[0]=5
print(a) #error
"""
# including integer , float , complex immutable also

# string slicing and string manipulation
"""
a="manipulation"
print(a[0:1])
print(a[0:2])
print(a[0:])
print(a[:-1])
print(a[-8:-1])
print(a[::-1])
"""
#String with keywords
"""
a=" Manipulation time"
print(len(a))
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.strip())
print(a.lstrip())
print(a.rstrip())
print(a.isalpha())
print(a.isupper())
print(a.islower())
print(a.startswith("M"))
print(a.endswith(""))
print(a.replace("p","M"))
print(a.title())
print(a.find("M",2))
print(a.find("o"))
"""
# concatination
"""
print("welcome" + "python")
"""

#append+=
"""
str1="welcome to "
str1+="learn python"
print(str1)
"""
#repeating
"""
str1="welcome "
print(str1*5)
"""
""""
str1="welcome to"
str2="to school"
str3=str1[:2]+str2[len(str2)-2:]
print(str3)
"""
# list concept
"""
a=[1,2,5,True,"ram",[1,2,3,4]]
print(a)
print(a[0])
print(a[4][2])
print(a.clear())
del a
"""
"""
a=[1,2,5,"d",3,2,2]
b=a.copy()
print(b)
print(b.count(2))
print(len(b))
#print(max(b)) #error
#print(min(b)) #error
b.remove(2)
print(b)
b.pop(4)
print(b)
b.append(40)
print(b)
b.extend([10,20,30])
print(b)
#b.sort(reverse=True)
print(b)
b.insert(0,"ram")
print(b)
print(b.index(2))
b.pop(4)
print(b)
"""
#Tuple concepts
"""
a=(1,2,5,"ram",True)
print(a)
print(type(a))
print(id(a))
b=list(a)
print(b)
c=(1)
print(type(c))
d=(1,)
print(type(d))


for i in a:   #loops
    print(i)

if 2 in a:     #if statement
    print("Value access")
else:
    print("Value not access")
#addiction
a=(1,2,3,4,5)
b=(1,2,3,4,5)
c=a+b
print(c)
"""
#set function
"""
a={10,"ram",12.5,True}
print(a)
a.add("kholi")
print(a)

b={10,20,"ajith",20.5}
a.update(b)
print(a)

for i in a:
    print(a)

a.remove(10)
print(a)

a.discard(20)
print(a)

a={10,20,30,40,50}
a.pop()
print(a)

a.clear()
print(a)

x={1,2,3,4,5}
y={2,3,4,5,6}
c=x.union(y)
print(c)

c=x.intersection(y)
print(c)

print(x-y)
"""
#Dictionary concepts
"""
a={

   "name":"kholi",
   "age":34,
   "gender":"male"
    }
print(a)
print(type(a))
print(a.keys())
print(a.values())
print(a["age"])
"""
# nested Dictionary
"""
b={
  "c":{
     "name":"ram",
     "age":23,
     "gender":"male"
      },
  "d":{
     "name":"jeeva",
     "age":21,
     "gender":"male"
      }
}
print(b)
print(type(b))
b.update({"name":"rajesh"})
print(b)
b["age"]=35
print(b)
"""
# If statement
"""
age=int(input("Enter your age:"))
if age>=18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")
"""
"""
number=int(input("Enter your number:"))
if number%2==0:
    print("This is even number")
else:
    print("This is not even number")
"""
"""
sub1=int(input("Enter your mark in first subject:"))
sub2=int(input("Enter your mark in second subject:"))
avg=(sub1+sub2)/2
if avg>=90:
    print("A grade")
elif avg<90 and avg>=80:
    print("B grade")
elif avg<80 and avg>=70:
    print("C grade")
elif avg<70 and avg>=60:
    print("D grade")
elif avg<60 and avg>=50:
    print("E grade")
else:
    print("Please enter your correct mark")
"""
"""
for i in range(1,20):
    vowels=input("Enter the letters:")
    if vowels in ("a","e","i","o","u","A","E","I","O","U"):
        print("This is vowels")
    else:
        print("This is not vowels")
"""
    #question
#0-->no fine
#1-5--->5 fine
#6-10-->10 fine
#11-30-->20 fine
#above 30-->membership canceled
"""
ldate=int(input("Enter you leave date:"))

if ldate==0:
    print("Fine no fees")
elif ldate>0 and ldate<=5:
    print("Fine is",ldate*5)
elif ldate>=6 and ldate<=10:
    print("Fine is",ldate*10)
elif ldate>=11 and ldate<=30:
    print("Fine is",ldate*20)
elif ldate>30:
    print("your membership canceld")
else:
    print("Please enter your correct leave date")
"""

#unit                 price
#first 100 unit       no charge
#next 100 unit        rs 5 per unit
#after 100 unit       rs 10 per unit
   #350 total bill = 2000
"""
unit = int(input("Enter your unit:"))
sum=unit-100

if unit<100:
    print("Suber no charge")
elif unit>100 and unit<=200:
    print("Your current bill is",sum*5)
elif unit>200:
    print("Your current bill is",sum*10-500)
else:
    print("Please enter your correct current bill")

"""

#find the lowest number out of three numbers
"""
num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
num3=int(input("Enter the number3:"))

if num1<num2 and num1<num3:
    print("num1 is the lowest number")
elif num2<num1 and num2<num3:
    print("num2 is the lowest number")
elif num3<num1 and num3<num2:
    print("num3 is the lowest number")
else:
    print("Please enter the corrrect number")
"""
#find the highest number out of three numbers
"""
for i in range(1,20):
    num1=int(input("Enter the number1:"))
    num2=int(input("Enter the number2:"))
    num3=int(input("Enter the number3:"))
    if num1>num2 and num1>num3:
        print("num1 is the highest number")
    elif num2>num1 and num2>num3:
        print("num2 is the highest number")
    elif num3>num1 and num3>num2:
        print("num3 is the highest number")
    else:
        print("Please enter the correct number")
"""
#write a program divided by 2 and 3
"""
num1=int(input("Enter the number:"))
if num1%2==0 and num1%3==0:
    print("The number is divided by 2 and 3 both")
else:
    print("The number is not divided by 2 and 3 both")
"""
#boiling point of water in 100 celcius
"""
temp=int(input("Enter the temprature:"))
if temp>=100:
    print("The water is boiling")
else:
    print("The water is not boiling")
"""
# highest age for 4 members (its lowest also )
"""
for i in range(1,20):
    age1=int(input("Enter the age first person:"))
    age2=int(input("Enter the age second person:"))
    age3=int(input("Enter the age third person:"))
    age4=int(input("Enter the age fouth person:"))

    if age1<age2 and age1<age3 and age1<age4:
        print("First person is young")
    elif age2<age1 and age2<age3 and age2>age4:
        print("Second person is young")
    elif age3<age1 and age3<age2 and age3<age4:
        print("third person is young")
    elif age4<age1 and age4<age2 and age4<age3:
        print("Fourth person is young")
    else:
        print("Please enter your correct age")
"""

  #mounment        city
   #---------        -----
  #red fort        delhi
  #taj mahal       agra
  #jal mahal       jaipur
"""
city=input("Enter the city name:")
if city.lower()=="delhi":
    print("Mounment name is : Red fort")
elif city.lower()=="agra":
    print("Mounment name is : Taj mahal")
elif city.lower()=="jaipur":
    print("mounment name is : Jal mahal")
else:
    print("Please enter your corrrect city")
"""

#Check the three digit number of middle
"""
num1=input("Enter the number:")
temp=len(num1)
if temp!=3:
    print("Enter three digit number")
else:
    print("middle digit is",(int(num1)%100//10))
"""
#even or add number
"""
num1=int(input("Enter the number:"))
if num1%2==0:
    print("This is even number")
elif num1%2!=0:
    print("This is the odd number")
else:
    print("please enter positive number")
"""

 #Market price           Discount
 #------------           --------
 #>10000                 20%
 #>7000 and <=10000      15%
 #<=7000                 10
"""
price=int(input("Enter your price:"))
if price>10000:
    print("Discount amount is",20/100*price)
    print(20/100*price-price)
elif price>7000 and price<=10000:
    print("Discount amount is",15/100*price)
elif price<=7000:
    print("Discount amount is",10/100*price)
else:
    print("Please enter correct price")
"""
#Nested if
"""
num = int(input("Enter the number:"))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
"""
"""
i = 13
  
if (i == 13): 
    #  First if statement 
    if (i < 15): 
        print ("i is smaller than 15") 
          
    # Nested - if statement 
    # Will only be executed if statement above 
    # it is true 
    if (i < 12): 
        print ("i is smaller than 12 too") 
    else: 
        print ("i is greater than 12 and smaller than 15")
"""

#loops
#1.for
#2.while

#for loops
"""
for i in range(1,20):
   # print(i)
    print(i,end="")
"""
"""
for i in range(2,20,2):
    print(i)
else:
    print("\n End of the loop")
"""
"""
for word in "computer":
    print(word,end="")
"""

# c co com comp  concept
"""
str1 = input("enter the string:")
index=1
for i in str1:
    print(str1[:index])
    index+=1

str2="computer"
index=1
for i in str2:
    print(str2[:index])
    index+=1
"""
#comp com co c reverse concepts
"""
str1=input("Enter the string:")
index=len(str1)
for i in str1:
    print(str1[:index])
    index-=1

str2="computer"
index=len(str2)
for i in str2:
    print(str2[:index])
    index-=1
"""

#alphapet concepts:
#A-Z--->65-90
#a-z--->97-122
"""
for i in range(65,91):
    print(chr(i),end="")

for i in range(97,123):
    print(chr(i),end="\n")
"""

#alphapet squre shape for loops
"""
n = int(input("Enter the number:"))
count=0
for i in range(n):
    for j in range(n):
        print(chr(65+count),end="")
        count+=1
    print()

n=int(input("Enter the number:"))
count=0
for i in range(n):
    for j in range(n):
        print(chr(97+count),end="")
        count+=1
    print()
"""
#same row same coulum Nested loops
"""
n=int(input("Enter the number:"))
for i in range(n):
    for j in range(n):
        print(chr(65+i),end="") #print(i)
    print()

n=5
for i in range(n):
    for j in range(n):
        print(chr(97+i),end="")
    print()
"""
"""
n=int(input("Enter the number:"))
for i in range(n):
    for j in range(n):
        print(chr(65+j),end="") #print(j)
    print()

n=5
for i in range(n):
    for j in range(n):
        print(chr(97+j),end="")
    print()
"""
#A AB ABC ABCD CONCEPT NESTED LOOPS
"""
for i in range(1,6):
    for j in range(65,65+i):
        print(chr(j),end="")
    print()

for i in range(1,6):
    for j in range(97,97+i):
        print(chr(j),end="")
    print()
"""
#ABCDE ABCD ABC AB A CONCEPT
"""
for i in range(6,0,-1):
    for j in range(65,65+i):
        print(chr(j),end="")
    print()

for i in range(6,0,-1):
    for j in range(97,97+i):
        print(chr(j),end="")
    print()
"""
# spesal charecter
"""
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

for i in range(1,7):
    for j in range(i):
        print("@",end="")
    print()

for i in range(1,7):
    for j in range(i):
        print("#",end="")
    print()
"""
# add string mathod
"""
str1="ABCDEFG"
str2="ate"
for i in str1:
    print((i+str2),end="\t")

str1="abcdefg"
str2="kholi"
for i in str1:
    print((i+str2),end="\t")
"""
#list in for loops
"""
list1=["car","bus","van","cycle"]
for i in list1:
    print(i)
else:
    print("No items left")
"""
"""
str1=input("Enter the string:")
str2="chennai"
if str2 in str1:
    print("Fount")
else:
    print("Not fount")
"""
#calculate the vowels and consonents
"""
str1=input("Enter a string:")
str2=("AEIOUaeiou")
v,c=0,0
for i in str1:
    if i in str2:
        v+=1
    else:
        c+=1
print("The given string contins {} vowels and {} consonents".format(v,c))
"""
#First 10 numbers 2 power values
"""
squre=[]
for i in range(1,11):
    s=i**2
    squre.append(s)
print(squre)
#another method

squre=[i**2 for i in range (1,11)]
print(squre)
"""
#first 20 numbers divided by 4 concepts
"""
div4=[]
for i in range(21):
    if i%4==0:
        div4.append(i)
print(div4)
"""
#positive numbers and nagative numbers
"""
numbers=(5,-8,6,8,-4,3,1)
positive=()
for i in numbers:
    if i>0:
        positive+=(i,)
print("Positive numbers:",positive)
"""

#while loops
"""
n=10
i=1
while i<=n:
    print(i)
    i+=1
print("Over over")
"""
#even and odd number in while concept
"""
n=int(input("Enter the number:")) #even
i=1
while i<=n:
    if i%2==0:
        print(i)
    i+=1
print("Over over")

n=int(input("enter the number:")) #odd
i=1
while i<=n:
    if i%2!=0:
        print(i)
    i+=1
print("Over  over")
"""
#k kh kho khol concept in while loop
"""
str1=input("Enter the string:")
index=1
while index<=len(str1):
    print(str1[:index])
    index+=1

str2="computer"
index=0
while index<=len(str2):
    print(str2[:index+1])
    index+=1
"""
"""
str1="*"
index=1
while index<=6:
    print(str1[:index])
    index+=1
"""
# sum of n numbers
"""
i=1
n=int(input("Enter the number:"))
sum=0
while i<=n:
    sum=sum+i
    i+=1
print(sum)
"""
#factorial number
"""
n=int(input("Enter the number:"))
i=1
fact=1
while i<=n:
    fact=fact*i
    i+=1
print("Factorial is",fact)
"""
#jump statement in python
"""
for word in "kholivox":   #break
    if word=="v":
        break
    print(word,end="")
else:
    print("\n end of the program")
print("\nEnd of the program")


for word in "kholivox":   #jump
    if word=="v":
        continue
    print(word)
else:
    print("end of the programme")


for word in "kholivox":    #pass
    if word=="v":
        pass
else:
    print("complete next time")

"""
# * ** *** **** ***** mathod in while loop
"""
str1="*"
i=1
while i<=5:
    print(str1*i)
    i+=1
"""

#list in while loop
"""
marks=[10,20,30,40,50]
i=0
while i<=5:
    print(marks[i])
    i+=1
"""
#reverse indexing
"""
marks=[10,20,30,40,50]
i=-1
while i>=-5:
    print(marks[i])
    i-=1
"""
#len concept in while
"""
sub=["tamil","english","maths","science"]
i=0
while i<=len(sub):
    print(sub[i])
    i+=1
"""
#armstrong number
"""
num1=int(input("Enter your number:"))
sum=0
temp=num1
while temp>0:
    digit=temp%10
    sum=sum+(digit**3)
    temp=temp//10
if num1==sum:
    print("Armstrong number")
else:
    print("Its not armstrong number")
"""
#reverse number
"""
num=int(input("Enter the number:"))
sum=0
while num>0:
    digit=num%10
    sum=sum*10+digit
    num=num//10
print("The reverse number is:",sum)
"""
#Palindrome number
"""
str1=input("Enter the string:")
str2=""
index=-1
for i in str1:
    str2+=str1[index]
    index-=1
print("The given string {}.The palindrome {}".format(str1,str2))
"""
#Prime number
"""
a=int(input("Enter the number:"))
fact=2
i=2
while a>i:
    if a%i==0:
        fact+=1
    i+=1
if fact==2:
    print("Prime number")
else:
    print("Not prime")
"""
#  functions or mathed

#no return type without argument function;
"""
def add():
    a=10
    b=20
    c=a+b
    print(c)
add()
"""
#no return type with arguments function:
"""
def add(a,b):
    c=a+b
    print(c)
add(10,20)
"""

#return type without arguments function:
"""
def mul():
    a=10
    b=10
    c=a*b
    return c
x=mul()
print(x)
"""
#return type with arguments function:
"""
def mul(a,b):
    c=a*b
    return c
x=mul(10,10)
print(x)
"""
#arbitary arguments function
"""
def course(*students):
    print(students)
    for i in students:
        print(i)
course("ram","raju","jeeva")
"""

#keyword aargument function
"""
def students(name,age):
    print(name,"age is",age)
students(age=25,name="vince")
"""
#arbitary arguments function
"""
def bio(**data):
    print(data)
bio(name="vince",age=21,gender="male")
"""
#default arguments function
"""
def user(name,city="madurai"):
    print(name,"city is",city)
user("kholi","chennai")
"""
#recursive function
"""
def fact(n):
    if n==1:
        return
    else:
        return n*fact(n-1)
print(fact(5))
"""
#logal andf global functions
"""
x=8
def loc():
    global x
    y="local"
    x=x*2
    print(x)
    print(y)
loc()
"""
"""
x=5
def loc():
    x=10
    print("local x:",x)
loc()
print("global x:",x)
"""

      #SOCIAL MEDIA IMPORTTANT QUESTION

#1:
"""
for num in range(10):
    if num<5:
        continue
    elif num>8:
        break
    print(num,end="")
"""

#2:
"""
numbers=[1,2,3,4,5]
for num in numbers:
    if num%2==0:
        continue
    print(num**2,end=" ")
"""
#3:
"""
i=0
while i<5:
    i+=1
    if i==3:
        continue
    print(i,end="")
"""
#4:
"""
numbers=[1,2,3,4,5]
result=[n for n in numbers if n%2==0]
print(result)
"""
#5:
"""
result=""
for i in range(1,11):
    if i%2==0:
        result+=str(i)+""
print(result)
"""
#6:
"""
for i in range(1,5):
    for j in range(i):
        if i%j==0:
            break
        else:
            print(i, end="") 
"""
#7:
"""
a=5
b=10
print((a>b and "a>b") or (b>a and "b>a"))
"""
#8:
"""
x,y=10,5
x,y=y+3,x-2
if x>y:
    print(x-y)
else:
    print(y-x)
"""

#9:
"""
def myfun(num):
    if num%2==0:
        return True
    else:
        return False
print(myfun(4))
"""
#10:
"""
def myfun(a,b,c):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return c
print(myfun(10,5,2))
"""
#11:
"""
def myfun(s):
    if len(s)==1:
        return s
    return myfun(s[1:]) +s[0]
print(myfun("python"))
"""
#12:
"""
a=5
b=7
c=a+b if a>b else b-a
print(c)
"""
#13:
"""
def myfun(x,y):
    if y==0:
        return 1
    else:
        return x*myfun(x,y-1)
print(myfun(2,4))
"""
#14:
"""
my_str= "python.hup"
print(my_str[-0])
"""
#15:
"""
def myfun(x,y):
    x=1
    y=1
    return x+y
print(myfun(3,4))
"""
#16:
"""
a=2
def multiply():
    b=3
    return a*b
print(multiply())
"""
#17:
"""
def myfun():
    pass
print(type(myfun()))
"""
#18:
"""
def python():
    return python()+1
print(python)
"""

#19:
"""
def x(values):
    values[0]=1
v=[2,3,4]
x(v)
print(v)
"""
#20:
"""
a=[0,1,2,3]
for a[-1] in a:
    print(a[-1])
"""

