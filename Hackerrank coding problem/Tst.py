def Fibo(n):
    List = [0,1]
    i,j,k = 0,1,1;
    while(k<=n-2):
        add = i+j;
        i=j;
        j=add;
        List.append(add);
    print(List)

n=int(input())
Fibo(n)    
