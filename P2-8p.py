def f(n):
    n= 20
    return n

n = 10

f(n)
print(n)

n = f(n)
print(n)

def plus(x):
    if x > 0:
        return True
    else :
        return False


n = int(input("정수 입력 :"))

print(plus(n))


def get_max(x,y):
    if x > y:
        return x
    else :
        return y

x =int(input(" 입력 "))
y =int(input(" 입력 "))

n = get_max(x,y)
print(n)

def get_sum(n):
    s = 0
    for i in range(n+1):
        s += i
    return s

q = int(input(" 정 수 입력:"))

print("1부터 %d까지의 합은 %d입니다." % (q,get_sum(q)))

def get_sum(x,y):
    s = 0
    for i in range(x,y+1):
        s += i
    return s

n = int(input(" a 부터?"))
m = int(input(" b 까지"))

print("%d부터 %d까지의 합은 %d입니다." % (n,m,get_sum(n,m)))

def area(x,y):
    return x*y

w = int(input(" 정수 입력 :"))
h = int(input(" 정수 입력 :"))

print(area(w,h))

def area(x):
    return 3.14 * x ** 2 

r = int(input(" 정수 입력 :"))

print(area(r))

def number(x):
    if x % 2 ==0:
        return "even"
    else :
        return "odd"
n = int(input("정수 입력 : "))

print(number(n))

def square(a,b):
    s = 1
    for i in range(b+1):
        s *= a
    return int(s/2)
n = int(input("정수 입력:"))
m = int(input("정수 입력:"))
##
##print(square(n,m))

def calculator(x,sb,y):
    if sb == '+':
        return x+y
    elif sb == '-':
        return x-y
    elif sb == '*':
        return x*y
    elif sb == '//':
        return x//y
    else :
        return "잘못 입력하셨습니다."

a = input("사칙 연산식을 입력하시오.: ").split()

a[0] = int(a[0])
a[2] = int(a[2])


print("%d %c %d = %d" % (a[0],a[1],a[2],calculator(a[0],a[1],a[2])))

