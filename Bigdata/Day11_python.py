print ("Hello world!")

help('len')

help('print') #주석달기

age = 20
name = 'swaroop'

print('{}was {}years old when he wrote this book'.format(name,age))
print('why is {} playing with that python?'.format(name))

print('{0:.3f}'.format(1.0/3))
print('{0:_^11}'.format('hello'))
print('{name} wrote {book}'.format(name='Swaroop',book='A Byte of Python'))

print("a",end=' ')
print('b')

print('This is the first line\nThis is the second line')
print(r"Newlines are indicated by \n")

i = 5
print(i)
#i = i + 1
i += 1
print(i)

s = '''This is a multi-line string. 
this is the second line'''
print (s)


length = 5
breadth = 2

area = length * breadth
print ('Area is', area)
print ('Perimeter is', 2 * (length + breadth))

number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    print('Congratylations, you guessed it.')
    print('but you do not win any prizes!')
elif guess < number:
    print("No, it is a little higher than that.")
else :
    print("No, it is a little lower than that.")

print("Done")


number = 23
running = True
while running:
    guess = int(input('Enter an interger:'))

    if guess == number:
        print ('Congratulations, you guessed it.')
        running = False
    elif guess < number:
        print ('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
        print ("the while loop is over.")
print ("Done")


for i in range(1,5):
    print (i)
else:
    print('The for loop is over')


while True:
    s = input('Enter something: ')
    if s == 'quit':
        break
    print ('Length of the string is', len(s))
print ('Done')


while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) <3:
        print ("Too small")
        continue
    print ("Input is of sufficient length")



def say_hello():
    print('hello world')

say_hello()

def print_max(a,b):
    if a>b:
        print (a, 'is maximum')
    elif a == b:
        print (a, 'is equal to', b)
    else:
        print(b, 'is maximum')


print_max(3,4)

x = 5
y = 7

print_max(x,y)

print_max(5,5)


x = 50

def func(x):
    print ('x is',x)
    x =2
    print ('Changed local x to',x)

func(x)
print ('x is still', x)

x = 50

def func2():
    global x
    
    print('x is', x)
    x = 2
    print ('Changed global x to', x)

func2()
print("Value of x is", x)


def say(message, times=1):
    print(message * times)

say("hello")
say("World", 5)



def func3(a, b=5, c=10):
    print ('a is', a, 'and b is', b, 'and c is', c)

func3(3,7)
func3(25,c=24)
func3(c=50,a=100)


def total(initial = 5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print (total(10, 1, 2, 3, vegetables=50, fruits=100))

def maximum(x, y):
    if x>y:
        return x
    elif x==y:
        return "The numbers are equal"
    else:
        return y

print (maximum(2,3))
print (maximum(3,3))

import sys

print ('The command line arguments are:')
for i in sys.argv:
    print (i)

print ('\n\nThe PYTHONPATH is', sys.path, '\n')

from math import sqrt
print("Square root of 16 is", sqrt(16))

if __name__ == '__main__':#만약 이 모듈 이름이 main이라면(바로 실행)
    print('This program is being run by itself')#사용자로부터 직접 실행된 것
else:#그렇지 않다면(import로 어딘가에서 끌어다 실행)
    print('I am being imported from another module')#다른 모듈에서 끌어온 것


def say_hi():    
    print ('Hi, this is mymodule speaking.')
__version__ = '0.1'






