#exception handling
# here put the condition which were the user is see the error is happening  or the possibility of the error
try: 
   x = int(input("enter the x: "))
   ans = 10/x

except ZeroDivisionError:
    print("you cant devide by the zero")

except ValueError :
    print("invalid input")

else :
    print(f"the ans is {ans}")  

finally:
    print("this is the end of the program")          


# for built in exception use the w3 schools website

