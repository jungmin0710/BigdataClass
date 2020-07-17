#오전수업_복습
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
##여기오류
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




#오전수업_
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

Number_System_change(325, 10, 7)
Number_System_change(5023,7,9)



import numpy as np #클래스로 임의의 자연수 문제 만들기
class Natural_number:
    def question(self):
        self.select = np.random.randint(5)
        self.n1 = np.random.randint(1,100)
        self.n2 = np.random.randint(1,100)
        self.n3 = np.random.randint(low = 2, high = 10)
        self.n4 = np.random.randint(low = 2, high = 30)
        if self.select == 0:
            print('{}가 소수인지 판별하고, 소수가 아니면, 약수를 구해라.'.format(self.n1))
        elif self.select == 1:
            print('{}와 {}의 최대공약수를 구하여라.'.format(self.n1,self.n2))
        elif self.select == 2:
            print('{}와 {}의 최소공배수를 구하여라.'.format(self.n3,self.n4))
        elif self.select == 3 :
            print ('{}를 2진법으로 나타내어라.'.format(self.n1))
        elif self.select == 4:
            self.n4_2 = digit_expand(self.n4,2)
            print('2진수 [{}]를 10진법으로 나타내어라.'.format(', '.join(map(str,self.n4_2))))

    def answer(self):
        if self.select == 0:
            if is_prime(self.n1):
                print('{}는 소수입니다.'.format(self.n1))
            else:
                print(factorization(self.n1))
        elif self.select == 1:
            print(greatest_common_factor(self.n1,self.n2,show=False))
        elif self.select == 2:
            print(least_common_multiple(self.n3,self.n4))
        elif self.select == 3:
            print(digit_expand(self.n1, 2))
        elif self.select == 4:
            print(digit_expand(self.n4,10))


q1 = Natural_number()
q1.question()
q1.answer()







#알고리즘 과제

try:
    n = eval(input("숫자를 입력하세요:"))
    if n - int(n) > 0:
        print("소수입니다.")
    else:
        print("정수입니다.")

except:
    print("math error")


#모범답안_위와 같다

try:
    num = eval(input("입력하시오."))
    if num - int(num):
        print("소수입니다.")
    else:
        print("정수입니다.")
except:
    print("math error")






