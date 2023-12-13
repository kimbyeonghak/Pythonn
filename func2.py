##from random import*
##
##def lotto():
##    lot = []
##
##    for i in range(6) :
##        lot.append(randint(1,45))
##
##    lot.sort()
##    print(lot)
##
##lotto()

##from random import*
##
##def lotto():
##    lot = set()
##
##    for i in range(6) :
##        lot.add(randint(1,45))
##
##    lot = list(lot)             ## n = int(n)
##    lot.sort()                  ## lot = list(lot)
##    print(lot)
##
##lotto()

##def func_abs(n):
##    if n > 0 :
##        return n
##    elif n < 0 :
##        return n*-1
##    else:
##        return "zero"
##n = int(input(" 정수 입력 : "))
##print(func_abs(n))

##def point(f):
##    l = n.split('.')
##    print(l[1])
##
##n = input("실수 입력:")
##point(n)

####def f(n):
####
####    for i in range(1,n+1):
####        for j in range(1,n+1):
####            print("%2d" % (i*j),end=' ')
####        print('')
####
####n = int(input(" 100 이하 정수 입력 : "))
####f(n)

##n = int(input(" 몇 단? "))
##
##for i in range(1,10):
##    print("%d"%(n*i))

##temp = 0
##def times_table(a,b):
##    a = int(a)
##    b = int(b)
##    
##
##    if a > b :
##        temp = a
##        a = b
##        b = temp
##
##    for i in range(a,b+1):
##        print("== %d Times ==" % i)
##        for j in range(1,10):
##            print("%d * %d = %d" %(i,j,i*j))
##        print()
##        
##a , b = input(" 정수 입력 : ").split()
##times_table(a,b)

#### 입력받은 소수 출력하기 ####

##n = int(input(" 정수 입력 :"))
##flag = 0
##
##for i in range(2,n+1):
##    cnt = True
##    for j in range(2, i):
##        if i % j == 0:
##            cnt = False
##    if cnt:
##        print(i, end = ' ' )
##

##n = int(input(" 정수 입력 :"))
##
##check = True
##
##for i in range(2,n):
##    if n % i == 0:
##        check = False
##
##print(check)


##a = int(input('a:'))
##
##for i in range(2,a+1):
##    check = True
##    for j in range(2,i):
##        if i%j==0:
##            check = False
##    if check :
##        print(i)

        
    
        
    

        


          

