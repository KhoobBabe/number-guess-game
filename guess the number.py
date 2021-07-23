import random
x= random.randint(1, 1001)
y= int(input("Enter a number between 1 and 1000: "))

while y>x or x>y:
    if y>x: 
        if (y-x)>200:
            print("Too High")
            y= int(input("Enter a number between 1 and 1000: "))
        elif (y-x)>10:
            print("high")
            y= int(input("Enter a number between 1 and 1000: "))
        elif (y-x)<=10:
            print("slightly high")
            y= int(input("Enter a number between 1 and 1000: "))
            
    if x>y:
        if (x-y)>200:
            print("too low")
            y= int(input("Enter a number between 1 and 1000: "))
        elif (x-y)>10:
            print("low")
            y= int(input("Enter a number between 1 and 1000: "))
        elif (x-y)<=10:
            print("slightly low")
            y= int(input("Enter a number between 1 and 1000: "))
        
    

if y==x:
    print("correct")
