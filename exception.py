a=int(input("Enter the number ")
b=int(input("Enter another number ")

try:
    print("RESOURCE OPENED")
    c=a/b                                       #when error occures except block gets excecuted
    print(c)
    d=int(input("Enter a number :: "))
    print(c/d)
except ValueError:
    print("CHECK OUT YOUR INPUT VALUE :) ")
except ZeroDivisionError:
    print("YOU CANT DIVIDE NUMBER WITH ZERO :)")
except Exception:
    print("OOPS SOMETHING WENT WRONG :( ")
finally:                                            #excecuted each and every time
    print("RESOURCE CLOSED")
print("BYE:)")
