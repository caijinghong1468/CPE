def algo(n):
    count = 0
    while(1):
        count += 1;
        if (n == 1):
            return count;
        elif (n % 2 == 1):
            n = 3*n+1;
        else:
            n=n/2;

hash_table = {}
try:
    while(1):
        i,j= map(int,input().split());
        if(i == 0 and j == 0):
            break;
        min_i = min(i,j);
        max_j = max(i,j);
        max_num = 0;
        for k in range(min_i,max_j+1):
            if k in hash_table:
                num = hash_table[k];
                if(k==min_i):
                    max_num = num;
                elif(num>max_num):
                    max_num = num;
            else:                
                count =algo(k);
                if(k==min_i):
                    max_num = count;
                elif(count>max_num):
                    max_num = count;
                
                hash_table[k] = count; 
        print(i,j,max_num);
except EOFError:
    pass