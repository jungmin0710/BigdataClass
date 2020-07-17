#알고리즘 숙제
#정석정답
while True:
    user=input("Input: ")
    string='abcdefghijklmnopqrstuvwxyz '
    number='0123456789'
    str=''
    int=''
    for i in user:
        if i in string or i in string.upper():
            str+=i
        if i in number:
            int+=i
    print("str: {}\nint: {}\n".format(str,int))

#유니코드로 문자열 분류하는 방법
inp = input("input:\n")  #ord: 문자 하나를 유니코드로 변환시켜 주는 함수
str=""
int=""
for i in range(0,len(inp)):
    if ord(inp[i])>47 and ord(inp[i])<58: #유니코드 48부터 57까지는 숫자(0~9)
        int+=inp[i]
    else:
        str+=inp[i]
print ("output\nstr:",str,"\nint:",int)


#########################################################
def is_prime(a):  #소수를 구하는 함수
    b = range(2,a)
    c = 0
    for i in b:
        if a % i == 0:
            c+=1
    if c>0:
        d = False
    else:
        d = True
    return d


def prime_factorization(a):  #소인수분해 함수
    b = range(2,a)
    prime = []
    for i in b:
        while a % i == 0:
            prime.append(i)
            a /= i
    if prime == []:
        prime.append(a)
    return prime


def factorization(a):  #약수 구하는 함수
    b = range(1,a)
    fac = []
    for i in b:
        if a % i == 0:
            fac.append(i)
    fac.append(a)
    return fac


def intersection(a,b): #교집합 구하는 함수
    c = []
    for i in a:
        if i in b:
            c.append(i)
    return c


def greatest_common_factor(a,b,show=False): #최대공약수 구하는 함수
    c = factorization(a)
    d = factorization(b)
    if show:
        print(c)
        print(d)
    e = intersection(c,d)
    return max(e)
a = 44
b = 78
greatest_common_factor(a,b)


def least_common_multiple(a,b): #최소공배수 구하는 함수
    c = prime_factorization(a)
    d = prime_factorization(b)
    for i in c:
        if i in d:
            d.remove(i)
    e = c + d
    f = 1
    for i in e:
        f *= i
    return f


def digit_expand(a,n): #n진수 구하는 함수
    digit = []
    while a // n != 0:
        e = a % n
        digit.append(e)
        a //= n
    digit.append(a)
    digit.reverse()
    return digit  


def Number_System_change(number, n, m): #n진법 숫자를 m진법으로 바꾸는 함수
    num_str = str(number)
    len_num = len(num_str)

    number_10 = 0
    for i, num in enumerate(num_str):
        num_int = int(num)
        if num_int >= n:
            print('{}는 {}보다 크거나 같으니 {}진법의 수가 아니다.'.format(num_int,n,n))
            break
        else:
            number_10 += num_int*n**(len_num-i-1) #10진법으로 바꾼다.
    number_m = digit_expand(number_10, m)
    return number_m

#########################################################
#오전수업

#Q1
#내 답
def list_to_number(a):
    sentence = ''
    for i in range(len(a)):
        sentence = sentence + a.pop(i) # pop은 안되나??
    sentence = int(sentence)
    return sentence

print (list_to_number([3,2,4,6,7,4,2,69]))
print (list_to_number([1,2,3,4]))





#정석 답
def list_to_number(a):
    sentence = ''
    for i in range(len(a)):
        sentence = sentence + str(a[i]) 
    sentence = int(sentence)
    return sentence

print (list_to_number([3,2,4,6,7,4,2,69]))
print (list_to_number([1,2,3,4]))



#Q2
#내 답
import numpy as np
a = []#난수의 리스트
c = 1
for i in range(0,5):
    b = np.random.randint(1,10)
    a.append(b)
    c *= b  #난수의 곱
    i += 1

print(a)
print(c)

#정석 답
n = 1
for i in range(5):
    temp = np.random.randint(1,10)
    print(temp,end=" ")
    n *= temp
print(temp)



#Q3
#내 답

def prime_factorization(a): #소인수분해
    b = range(2,a)
    prime = []
    for i in b:
        while a % i == 0:
            prime.append(i)
            a /= i
    if prime == []:
        prime.append(a)
    return prime

import numpy as np

def least_common_multiple(a,b): #최소공배수
    c = prime_factorization(a)
    d = prime_factorization(b)
    for i in c:
        if i in d:
            d.remove(i)
    e = c + d
    f = 1
    for i in e:
        f *= i
    return f

a = [] #난수 두개 만들 리스트
for i in range(2): 
    i = np.random.randint(10,100)
    a.append(i)

print(a)
print(least_common_multiple(a[0],a[1])) #답




#Q4
#내 답

for i in range(1,100):
    if i % 6 == 3 and i % 8 == 5 and i % 9 == 6:
        print(i)




#Q5
#내 답

for i in range(1,100):
    if i == 1:
        pass
    elif i % 4 == 1 and i % 5 == 1 and i % 6 == 1:
        print (i)


#Q6
#내 답
def list_to_number(a):
    number = ''
    for i in range(len(a)):
        number = number + str(a[i])
    number = int(number)
    return number


def digit_expand(a, n):
    digit_n = []
    c = 0
    while a // n != 0:
        c = a % n
        digit_n.append(c)
        a //= n

    digit_n.append(a)
    digit_n.sort()
    return digit_n

digit_expand(234,10)

def Number_system_change(number,n,m):
    num_str = str(number)
    len_num = len(num_str)

    number_10 = 0
    for i, num in enumerate(num_str):
        num_int = int(num_int)
        if num_int >= n:
            print('{}는 {}과 크거나 같으니 {}진법의 수가 아니다.'.format(num_int, n,n ))
            break
        else:
            number_10 += num_int*n**(len_num-i-1)
    number_m = digit_expand(number_10, m)
    return number_10    






a = Number_system_change(621, 7, 10)
b = Number_system_change(3213, 4, 10)
a = list_to_number(a)
b = list_to_number(b)
print (a)
print (b)
print ('{}개의 수가 있다.'.format(a-b))



#알고리즘 숙제
#세 모서리 길이가 각각 48, 60, 72cm인 직육면체모양의 나무토막을 잘라서 될 수 있는 한 큰 정육면체 모양의 나무토막으로 나누려고 한다. 이때 정육면체모양의 나무토막은 모두 몇 개가 생기는지 구하시오.
#힌트: 세 수의 최대공약수를 구하세요.






