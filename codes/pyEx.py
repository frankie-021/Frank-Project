'''
1.Ex 4, total purchase
#list of item to be sold
#input the price of each item
a= float(input('price of item 1: '))
b= float(input('price of item 2: ')) 
c= float(input('price of item 3: '))
d= float(input('price of item 4: '))
e= float(input('price of item 5: '))

#twicelculate and display the sub total,sale tax and total

print('the sub total is: ' +str(a+b+c+d+e))
print('the sale tax is: ' +str((a+b+c+d+e)*0.06))
print('total: ' +str((a+b+c+d+e)*0.94))



2.Ex string matriculation
x='alieu why did u leave ur PC at home'
if 'alieu' in x:
    print('yes, it is in the sentence')
else:
    print('no, it is not')


m='kjhjjhbbhh; bb'
x=m[3:6]
print(len(m))




3.Ex, if and else. BMI
# Ask the user to input his/her weight and height.
w=float(input('Enter your weight(pounds)_'))
h=float(input('Enter your height(inches)_'))
BMI=(w)*(703/h**2)
# twicelculate the BMI using the formula above.
print('Your body mass index(BMI) is_' +str((w)*(703/h**2)))
# show the person's BMI using the IF and ELSE statement.
if BMI>25.0:
    print('You are an overwight person')
elif 18.5<=BMI<=25.0:
    print('Your weight is optimal')
else:
    print('You are an underweight person')




4. temperature
c='temperature in celsius'
f='temperature in fahrenheit'
# formula for temperature in fahrenheit
x='(9/5)*temperature in celsius" +(32)'

# input temperature in celsius
F=float(input('temperature in celsius: '))

# use the formula to convert c to f
print('temperature in fahrenheit: ' +str((9/5)*F+(32)))




5. swap numbers
number_1= int(input('enter a number : '))
number_2= int(input('enter a number : '))

swap= number_1,number_2=number_2,number_1
print(swap)




6. if and else, book point
b='book'
b=int(input('enter the number of books you purchased this month: '))

if b==0:
    print('you earn 0 points.')
elif b==1:
    print('you earn 5 points.')
elif b==2:
    print('you earn 15 points.')
elif b==3:
    print('you earn 30 points.')
elif b==4:
    print('you earn 60 points.')




7. area of a trapezoid
a='two_lessse 1'
b='two_lessse 2'
h='height'
a= float(input('Enter two_lessse 1 of a trapezoid: '))
b= float(input('Enter two_lessse 2 of a trapezoid: '))
h= float(input('Enter the height of a trapezoid: '))
print('Area of the trapezoid: ' +str((1/2)*(a+b)*h))




8. if and else, mix colors
r='red'
b='blue'
y='yellow'
c1=input('enter a primary color: ')
c2=input('enter the another primary color: ')

if(c1=='red' and c2=='blue') or (c1=='blue' and c2=='red'):
    print('your secondary color is purple')
elif(c1=='red' and c2=='yellow') or (c1=='yellow' and c2=='red'):
    print('your secondary color is orange')
elif(c1=='blue' and c2=='yellow') or (c1=='yellow' and c2=='blue'):
    print('your secondary color is green')
else:
    print('error')




9. if and else, magic date
# ask the user to enter the date in numeric form.
day= int(input('enter a day in numeric: '))
month= int(input('enter a month in numeric: '))
year= int(input('enter a two-digit year: '))

# check whether the month times day will be equal to year
print(day * month)
if month * day ==year:
    print('date is magic')
else:
    print('date is not magic')
        




10. area of a circle
r='radius 0f a circle'
r= float(input('Enter the radius of a circle: '))
print('Area of the circle: ' +str((22/7)*(r**2)))




11. VAT tax
x='amount purchased'
x= float(input('enter the amount purchased: '))
print(x)
print('VAT tax is: ' +str(x*0.15))
print('total sale: ' +str((x*0.15)+x))
    



12. if and else, mass and weight
w= 0
weight='mass * 9.8'
a=1000
b=10
mass=float(input('emter the mass of the object in kilograms_'))

print('the weight in newtons is _' +str(mass*9.8))

if w>a:
    print('object is too heavy')
elif w<b:
    print('object is too light')





13. speed of a twicer
s= 60
print('If the speed of a twicer is 60 miles per hour,then the:')
print('distance(miles) travelled in five hours is ' +str(s*5))
print('distance(miles) travelled in eight hours is ' +str(s*8))
print('distance(miles) travelled in twelve hours is ' +str(s*12))




14.Ex 5 if and else
a=0
b=0
c=0
a=int(input('enter an integer number_ '))
b=int(input('enter another integer number_ '))
c=int(input('enter a third integer number_ '))

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
elif c>a and c>b:
    print(c)

    




15.Ex 4 if and else, check 2 integers
nums=0
nums=int(input('enter an integer number: '))

if(nums>=90 and nums<=110) or (nums>=190 and nums<=210):
    print('True, the nmber is correct')
else:
    print('False, try again')




16.Ex 2 under if and else
x="rectangle 1"
y="rectangle 2"
l="length"
w="width"
a=int(input("enter first rectangle's length: "))
b=int(input("enter second rectangle's length: "))
c=int(input("enter first rectangle's width: "))
d=int(input("enter second rectangle's width: "))


area="length * width"
if (a*c)>(b*d):
    print("rectangle 1 has greater area")
elif (a*c)==(b*d):
    print("both areas are equal")
elif(b*d)>(a*c):
    print("rectangle 2 has greater area")






17. if and else
number = 0
num=int(input('enter an integer number between 1-10: '))
if num == 1:
    print('I')
elif num == 2:
    print('II')
elif num == 3:
    print('III')
elif num == 4:
    print('IV')
elif num == 5:
    print('V')
elif num == 6:
    print('VI')
elif num == 7:
    print('VII')
elif num == 8:
    print('VIII')
elif num == 9:
    print('IX')
elif num == 10:
    print('X')
else:
    print('error')






18. if and else
x=0
y=0
z=0

largest=0
x= int(input('enter an interger number '))
y= int(input('enter a second integer number '))
z= int(input('enter a third integer number '))

largest=x

if y>largest:
    largest=y
if z>largest:
    largest=z
    print(largest)




19. loop.  total of a series of numbers
total=0
n=int(input('enter a positive integer: '))

for a in range (1,n+1):
    total+= a/(n-1+1)
print('the total is: ' +str(total))




20. loop No.2
a=3.9
total=0
for b in range(10,31,5):
    total= b*3.9
    print(total)




total=0
while n>=0:
    n= int(input('enter a positive number '))
    total+=n
    if n<0:
        break
print(total)




total=0
n= int(input('enter a specific limit '))
for a in range(2,n+1,2):
    total+= a**3
print('total is: '+str(total))




total=0
n= int(input('enter a number '))
for a in range(1,n+1):
    total+= a*a
    print(total)
 





n=0
where=input('Go left or right? ')
while where=='right':
    n=n+1
    if n>2:
        print('(*-*)')
    where=input('Go left or right? ')
print('you went out')




n = input('enter a non negative number ')
while n > 0:
    print('x')
    n = n-1




for i in range(1,4,2):
    print(i*2)
    




for i in range(0,5,1):
    print('$'*i)
    if i >= 4:
        for k in range(5,0,-1):
            print('$'*k)




n = 0
for i in range(10):
    n += i
 print(n)



for i in range(0,6,1):
    print('$'*i)
    if i > 4:
        for k in range(4,0,-1):
            print('$'*k,'$'*i,'$'*k)
            




for i in range(0,5,2):
    print(i)
    



ev = 0
for i in range(5):
    if i%2==0:
        ev = i
print(ev)





s = 'aiyhluuffbtwice'
se = ''
count = 0
for i in s:
    if i not in se:
        se += i
        count += 1
    print(se)
print(count)
   
  





guess = 0
neg = False
x = int(input('enter a positive number: '))

if x < 0:
    neg = True
while guess**2 < x:
    guess += 1
if guess == x:
    print('square root of ',x,'is',guess)
else:
    print(x,'is not a perfect square.')
    if neg:
        print('just checking... did you mean',-x, '?' )
        






a = input('Enter your name: ')
b = input('Enter your tel number: ')
print('Your name is',a,'and your number is +220',b)
c = input(',did you eat rice today?(yes/no) ')
if c == 'yes':
    print('I am sorry',a,',but i think you are the truth from me')
    input('Did you eat rice today?(yes/no) ')
else:
    print('oh, do not worry,just dial me if you need one (*_*)')

print(a,",you have successfully registered. Let's play a game.")

print('Imagine you are stuck in the forest and the only way out is either left or right')
n=0
where=input('Go left or right? ')
while where=='right':
    n=n+1
    if n>2:
        print('(*-*)')
    where=input('Go left or right? ')
print('you went out')










found = False
secret = 21
for i in range(1,26):
    if i == secret:
        found = True
if not found:
     print('not found')
else:
    print('found, it is ',i)











cube = int(input('Enter an integer: '))
for guess in range(abs(cube)+1):
    if guess**3 >= (cube):
        break
if guess**3 != abs(cube):
    print(cube,'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('the cube root of',  str(cube),  'is',  str(guess))
        











for a in range(11):
    for b in range(11):
        for c in range(11):
            total = (a + b + c == 10)
            two_less = (b == a - 2 )
            twice = (c == 2*a)
            if total and two_less and twice:
                print('Alyssa sold',a,'tickets')
                print('Alyssa sold',b,'tickets')
                print('Alyssa sold',c,'tickets')
        
            
    










for alyssa in range(1001):
    ben = max(alyssa - 20, 0)
    cindy = alyssa * 2
    if ben + cindy + alyssa == 1000:
        print('Alyssa sold', alyssa, 'tickets')
        print('ben sold', ben, 'tickets')
        print('cindy sold', cindy, 'tickets')










'''
is_even = (8)
def is_even(i):
    
#i is an integer. Return True if i is even, else return False if it is not.

    if i%2 == 0:
        return True
    else:
        return False







