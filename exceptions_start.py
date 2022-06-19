# Errors can happen in programs, and we need a clean way to handle them
# TODO: This code will cause an error because yu can't divide by zero
# x= 10/0 
# TODO: Exception provode a way of catching errors and then handling them
try:
    x = 10/ 0
except:
    print("well that didn't  work")
# a seprate  section of the code to group them together
# TODO: you can also catch specific exceptions
try:
    answer = input("what should I divide 10 by?")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("You can't divide by zero!")
except ValueError as e:
    print("You didn't give me a valid number!")
    print(e)
