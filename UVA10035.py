while True:
    c=0;
    count = 0;
    a,b = map(int ,input().split());
    if(a == 0 and  b == 0 ):
        break;
    else:
        while True:
            if(a==0 and b==0):
                break;
            elif((a%10 + b%10+c) > 9):
                count += 1;
                c =1;
                a = a//10;
                b = b//10;
            else:
                c=0;
                a = a//10;
                b = b//10;
    if(count == 0):
        print("No carry operation.");
    elif(count == 1):
        print(f"{count} carry operation.");
    else:
         print(f"{count} carry operations.");
