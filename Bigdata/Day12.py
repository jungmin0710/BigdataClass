#알고리즘 과제
def search(x,y,z):
    if x + y + z == 180 and int(x)>0 and int(y)>0 and int(z)>0:
        if x < 90 and y < 90 and z < 90:
            result = print('예각삼각형')
        elif x == 90 or y== 90 or z== 90:
            result = print('직각삼각형')
        elif x > 90 or y > 90 or z > 90:
                    result = print('둔각삼각형')
    else:
        result = print('삼각형이 아니다.')

    return ''

x=int(input('제1각을 입력하세요'))
y=int(input('제2각을 입력하세요'))
z=int(input('제3각을 입력하세요'))
    
print(search(x,y,z))


#모범답안

def search (x,y,z):
    if x+y+z !=180 or x == 0 or y == 0 or z ==0:
        print('삼각형이 아닙니다')
    else:
        if max(x,y,z)>90 :
            print('둔각삼각형입니다')
        elif max(x,y,z) == 90:
            print('직각삼각형입니다')
        else:
            print('예각삼각형입니다')
    return ''

x=int(input('제1각을 입력하세요'))
y=int(input('제2각을 입력하세요'))
z=int(input('제3각을 입력하세요'))
    
print(search(x,y,z))   




#오전수업내용


a = 17
b = range(2,a)
c = []
for i in b:
    while a % i == 0:
        c.append(i)
        a = a / i
if len(c) == 0:
    c.append(a)

print(c)

def prime_factorization(a):  #소인수분해
    b = range(2, a)
    primes = []
    for i in b:
        while a % i == 0:
            primes.append(i)
            a = a / i
    if primes == []:
        primes.append(a)

    return primes


print(prime_factorization(128))
print(prime_factorization(497))
print(prime_factorization(10135867))
print(prime_factorization(17))

a = 24
b = range(1,24)
factor = []
for i in b:
    while a % i == 0:
        factor.append(i)
factor.append(a)
print(factor)

def factorization(a):  #약수구하기
    b = range(1,a)
    factor = []
    for i in b:
        if a % i == 0:
            factor.append(i)
    factor.append(a)
    return factor
    







def intersection(a,b):  #교집합 구하기
    c = []
    for i in a:
        if i in b:
          c.append(i)
    return c  

def greatest_common_factor(a,b,show=False):  #최대공약수 구하기
    c = factorization(a)
    d = factorization(b)
    if show :
        print(c)
        print(d)
    e = intersection(c,d)
    return max(e)

a = 36
b = 96
print(greatest_common_factor(a,b))



def least_common_multiple(a,b):  #최소공배수 구하기
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



print(least_common_multiple(36,96))
print(least_common_multiple(4,7))



a = 325
digit_10 = []
while a // 10 != 0:
    e = a % 10
    digit_10.append(e)
    a //= 10
digit_10.append(a)
print(digit_10)
digit_10.reverse()
print(digit_10)
            

def digit_expand(a,n):  #n진수 만들기
    digit = []
    while a // n != 0:
        e = a % n
        digit.append(e)
        a //= n
    digit.append(a)
    digit.reverse()
    return digit

a = digit_expand(1732,10)
print(a)

a = digit_expand(11,2)
print(a)

a = digit_expand(1732,2)
print(a)

print(digit_expand(1732,7))
print(digit_expand(1732,9))

#알고리즘












