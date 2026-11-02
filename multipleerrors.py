try:
    num1 = int(input("enter the first number :"))
    num2 = int(input("enter the second number:"))
    result = num1 / num2
    print("result is", result)

except ZeroDivisionError:
    print("division by zero is error!!!")
except ValueError:
    print("pls enter valid whole numbers ")
except:
    print("wrong input")
else:
    print("no exception")
finally:
    print("this will execute no matteer what")