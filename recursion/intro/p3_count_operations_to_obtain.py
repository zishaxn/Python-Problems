def countOperations(num1, num2):
    if num1==0 or num2==0:
        return 0
    if num1>num2:
        return 1 + countOperations(num1-num2,num2)
    else:
        return 1 + countOperations(num1,num2-num1)

print(countOperations(10,5))