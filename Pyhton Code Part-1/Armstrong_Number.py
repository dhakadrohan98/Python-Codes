num = int(input('enter a number: '))
order = len(str(num))
sum=0; q = num;
while q>0:
    sum+=(q%10)**order
    q//=10
if(sum==num):
 print('A')
else:
    print("NOt A")
