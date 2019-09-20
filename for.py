'''
For Loop:
    1.Syntax:
            for i in range(number) //i start with 0 and
                ....code....
                ....code....
    In range one parameter is mandatory.
'''
#To print 0 to 9
#i is initialize with 0 and 10 is exclude from loop
for i in range(10):
        print(i)

#When want to start with 1
for i in range(1,10):
        print(i)

#to take interval
for i in range(1,10,2): #third parameter to interval
    print(i)

for i in range(10,1,-1): #third parameter to interval
    print(i)


#To break loop at specific condition
for i in range(1,10):
    if i==5:
        break
    else:
        print(i)

#To pass loop at specific condition
for i in range(1,10):
    if i==5:
        continue
    else:
        print(i)

#To print number which divisible by 3
for i in range(1,22):
    if i%3==0:
        print(i)

#To print List using for loop
a=[10,20,30,40]
print(a)
for i in a:
    print(i)

#To print Tuple using for loop
b=(10,20,30,40)
print(b)
for i in b:
    print(i)


'''
python base project work on Rasberry pi (Rs 3500)
other than rasberry pi cost rs 200
ardino board (Rs 200) use embedded c
medicine box
emergency robot
emotion base music player
'''