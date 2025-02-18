
while(1):
    num = int(input())
    if num == 0 :
        break
    n = num
    sum = 0
    count = 1
    while n != 0:
        if count % 2 == 1: 
            sum += (n % 10)
            n = n // 10
        else:
            sum -= (n % 10)
            n = n // 10
        count += 1 
    if num % 11 == 0 :
        print(f"{num} is a multiple of 11.")
    else:
        print(f"{num} is not a multiple of 11.")