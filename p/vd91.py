n=int(input("n="))
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i

if s==n:
    print(n, " n là số hoàn hảo")
else:
    print(n, " n không là số hoàn hảo")
