import sys
def main():
    i=sys.stdin.readline();
    for _ in range(int(i)):
        num = list(map(int,input().split())); 
        length = num[0];      
        new_list = sorted(num[1:]);
        if(length%2 == 1):
            print(count(num,new_list[int(length//2)]));
        else:
            print(count(num,new_list[length//2]));



def count(arr,num):
    sum=0
    for i in range(arr[0]):
        sum+= abs(num - arr[i+1]);
    return int(sum);
if __name__ == "__main__":
    main();         