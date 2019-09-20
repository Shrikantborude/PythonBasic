'''
While Loop:
    1.Syntax:
        while (exp):     () is optional.
            ...code...
            ...code...
Increment(x++) and Decrement(a--) is not Supported in Python.
Drawback:
        We have initialize one variable.
        continue in not working in while.
'''

#code to print 'Hey' 5 times.
a=1;
while a<=5:
    print("Hey")
    a=a+1

#To Print 5 to 1
a=5;
while a>=1:
    print(a)
    a=a-1

#To print "Hii" 5 times through function
def hii():
    print("Hii")
a=1
while a<=5:
    hii()
    a=a+1

#To break a program at specific condition
a=1
while a<=10:
    if a==8:
        break
    else:
        print(a)
    a=a+1

#To pass a specific condition in program
a=1
while a<=10:
    if a==8:
        pass
    else:
        print(a)
    a=a+1
