def spl(n,stack):
    if n >10000000:
        spl(n)

count = 1
while True:
    try:
        stack = []
        num=int(input())
        if num == 0:
            print(f"{count}. 0")
        else:
            spl(num,stack)
            print(f"{count}. {" ".join(stack)}")
        count += 1
    except EOFError:
        break