while True:
    try:
        arr = input().split()
        print(abs(int(arr[0]) - int(arr[1])));
    except EOFError:
        break;
        