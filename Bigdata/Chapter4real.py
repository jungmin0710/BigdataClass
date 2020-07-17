

def add(a,b):
    return a+b



a = 3
b = 4
c = add(a,b)
print(c)



def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1,2,3)
print(result)

def add_mul(choice,*args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result*i
    return result


result = add_mul('add',1,2,3,4,5)
print(result)

result = add_mul('mul',1,2,3,4,5)
print(result)


def add_and_mul(a,b):
    return a+b,a*b

result1, result2 = add_and_mul(3,4)

print(result1)


def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, True)



say_myself("박응선", 27, False)



a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)

def vartest(a):
    a = a +1

vartest(3)
print(a)

a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

a = 1
def vartest():
    global a
    a = a+1

    vartest()
    print(a)


add = lambda a,b: a+b
result = add(3,4)
print(result)



number = input("숫자를 입력하세요:")
print(number)

for i in range(10):
    print(i, end=' ')

f = open("새파일.txt",'w')
f.close()

f = open("C:/새파일.txt", 'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close


f = open("C:/새파일.txt",'r')
line = f.readline()
print(line)
f.close

f = open("C:새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()



f = open("C:/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("C:/새파일.txt", 'r')
data = f.read()
print(data)
f.close()


f = open("C:/새파일.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()



with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")



def is_odd(i):     
    if i % 2 == 1 :
        return True
    else:
        return False
    

is_odd(3)




def average(*args):
    sum = 0
    for i in args:
        sum += i
    return sum / len(args)
    
average(1,2)




input1 = input("첫번째 숫자를 입력하세요:") #input으로 숫자를 입력하면 문자열 취급을 받음
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)




#사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
user_input = input("저장할 내용을 입력하세요:")
f = open("C:/사용자입력파일.txt",'a')
f.write(user_input)
f.write("\n")
f.close()



class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))




class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


a = FourCal()
a.setdata(4,2)
print(a.first)
print(a.second)

b = FourCal()
b.setdata(3,7)
print(b.first)


print(a.add())
