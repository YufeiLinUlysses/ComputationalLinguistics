def fib1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

print(fib1(40))

def fib2(n):
    count = 1
    temp1 = 1
    sum = 1
    while(count <= n):
        if count == 1 or count == 2:
            sum = 1
            count += 1
        else:
            temp2 = sum
            sum += temp1
            temp1 = temp2
            count += 1
    return sum

print(fib2(40))