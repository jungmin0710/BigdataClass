#ncs1


a = 17
a_prime = True
for i in (2,a):
    if a % i == 0:
        a_prime = False

if a_prime == True:
    print('{}는 소수이다.'.format(a))
else:
    print('{}는 소수가 아니다.'.format(a))


def is_prime(a):
    b = range(2,a)
    c = 0
    for i in b:
        if a % i == 0:
            c+=1
    if c>0:
        print('{}는 소수가 아니다.'.format(a))
        d = False
    else:
        print('{}는 소수이다.'.format(a))
        d = True
    return d

is_prime(31)
is_prime(18)



def is_prime2(a):
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
 



a = range(1,101)
prime_numbers = []
for i in a:
    c = is_prime2(i)
    if c == True:
        prime_numbers.append(i)
print(prime_numbers)


a = range(2,1001)
prime_list = [1]
diff = 0

for i in a:
    c = is_prime2(i)
    if c == True:
        prime_list.append(i)
    if prime_list[-1] -prime_list[-2] > diff:
        diff = prime_list[-1] - prime_list[-2]
        max_diff_primes = [prime_list[-2], prime_numbers[-1]]

print('소수사이 구간의 최대값 : {}' .format(diff))
print('최대구간의 소수쌍 : {}'.format(max_diff_primes))


a = 17
b = range(2,a)
List = []
for i in b:
    while a % i ==0:
        List.append(i)
        a = a / i
        
if len(List) == 0:               #or if List = []:
    List.append(a)               

List



#알고리즘 : 해시탐색법으로 데이터를 탐색하는 알고리즘(탐색)/단순선택법(정렬)


def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for k in range(i+1,len(arr)):
            if arr[k] < arr[min_index]:
                min_index = k
        tmp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = tmp
    return arr


test = [12,13,11,14,10]
print(selection_sort(test))


#알고리즘 과제
def search(x,y,z):
    if x + y + z == 180 and int(x)>0 and int(y)>0 and int(z)>0:
        if x<90 and y<90 and z<90:
            result = print('예각삼각형')
        elif x ==90 or y==90 or z==90:
            result = print('직각삼각형')
        elif x >90 or y>90 or z>90:
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






