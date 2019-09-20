'''user=input("Enter your username")
#passw=input("Enter Your Password")
user=int(user)
if user>5:
    if user>=8:
        print("Near to 10")
    else:
        print("Far from 10")
else:
    print("Less than 5")
'''
a=int(input("Enter 1st Number\t"))
b=int(input("Enter 2nd Number\t"))
c=input("Operation\t")
if c=='+':
    print("Addition:",a+b)
elif c=='-':
    print("Substraction:",a-b)
elif c == '*':
        print("Multiplication:",a*b)
elif c == '//':
        print("Division in Integer:",a//b)
elif c == '/':
        print("Division in Float:",a/b)
elif c == '%':
        print("Division in Integer:",a%b)
