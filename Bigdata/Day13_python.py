
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input("Enter text: ")
if is_palindrome(something):
    print ("Yes, it is a palindrom")
else:
    print ("No, it is not a palindrome")







poem = '''\
Programming is fun
when the work is done
if you wanna make your work also fun:
    use Python!
'''

f = open('poem.txt','w') #텍스트로 저장
f.write(poem)
f.close()

f = open('poem.txt')
while True:
    line = f.readline()

    if len(line) == 0 :
        break

    print (line,)
f.close



import pickle
shoplistfile = 'shoplist.data'
shoplist = ['apple','mango','carrot']

f = open(shoplistfile, 'wb') #얘는 바이너리로 저장됨. 

pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile, 'rb')

storedlist = pickle.load(f)
print (storedlist)



"hello world"
type ("hello world")
u"hello world"
type(u"hello world")


#encoding=utf-8    #한글이 깨질 경우 유니코드형식 적용해주어야 함
import io

f = io.open("abc.txt","wt", encoding="utf-8")
f.write(u"Imagine non-Englishlanguage here. ㅎㅅㅎ")
f.close()

text = io.open("abc.txt", encoding="utf-8").read()
print (text)



try:
    text = input('Enter something -->')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))


class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something -->')
    if len(text) < 3 :
        raise ShortInputException(len(text), 3)

except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print('ShortInputException: The input was' + \
        ' {0} long, expected at least {1}'\
        .format(ex.length, ex.atleast))
else:
    print ('No exception was raised.')



#읽어 올 때 마다 2초씩 멈추기
import sys
import time

f = None
try : 
    f = open("poem.txt")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print (line,)
        sys.stdout.flush()
        print("Press ctrl+c now")
        time.sleep(2)
except IOError:
    print ("Could not find file poem.txt")
except KeyboardInterrupt:
    print ("!! You cancelled the reading from the file.")
finally: #예외가 발생해도 finally를 쓰면 꼭 수행한다.
    if f:
        f.close()   #예외가 발생해도 파일은 꼭 닫아줘야한다
    print("Cleaning up:Closed the file")





with open('poem.txt') as f: #with로 파일 열면 close를 따로 적지않아도 자동으로 닫아줌
    for line in f:
        print (line,)





import os, platform, logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')

print("Logging to", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w'
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")


def get_error_details():
    return(2,'details')

errnum, errstr = get_error_details()
errnum
errstr


a = 5; b = 8
a,b
a,b = b,a
a,b

flag = True
if flag: print ('Yes')


points = [ {'x' : 2, 'y' : 3}, {'x' : 4, 'y' : 1}]
points.sort(key=lambda i : i['y'])
print (points)


listone = [2,3,4]
listtwo = [2*i for i in listone if i >2]
print (listtwo)



def powersum(power, *args):
    '''Return the sum of each argument raised to the specified power.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total

powersum(2,3,4)
powersum(2,10)




mylist = ['item']
assert len(mylist) >= 1
mylist.pop()
assert len(mylist) >= 1



from time import sleep
from functools import wraps
import logging
logging.basicConfig()
log = logging.getLogger("retry")

def retry(f):
    @wraps(f)
    def wrapped_f(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                return f(*args, **kwargs)
            except:
                log.exception("Attempt %s/%s failed : %s",
                attemptm,
                MAX_ATTEMPTS,
                (args, kwargs))
                sleep(10*attempt)
        log.critical("ALL %s attempts failed : %s",
        MAX_ATTEMPTS,
        (args, kwargs))
    return wrapped_f

counter = 0
@retry
def save_to_database(arg):
    print("Write to a database or make a network call or etc.")
    print( "This will be automatically retried if exception is thrown.")
    global counter
    counter += 1
    if counter < 2:
        raise ValueError(arg)
    if __name__ == '__main__':
        save_to_database("Some bad value")

