a=[1,2,5,10]
n=int(input())
t=int(input())//100
dp=[[[-1 for i in range(n+1)] for j in range(t+1)] for k in range(5)]
def solve(la,n,t,b):
    if t==0:
        dp[la][t][n]=0
        return dp[la][t][n]
    elif la==0 or n==0:
        dp[la][t][n]=-(10**10)
        return dp[la][t][n]
    if dp[la][t][n]==-1:
        if a[la-1]<=t and b[la-1]>=1:
            c=b.copy()
            b[la-1]-=1
            dp[la][t][n]=max((1+solve(la,n-1,t-a[la-1],b)), solve(la-1,n,t,c))
            return dp[la][t][n]
        else:
            dp[la][t][n]=solve(la-1,n,t,b)
            return dp[la][t][n]
    else:
        return dp[la][t][n] 
    
b=[]    
for i in range(4):
    b.append(int(input()))

m=solve(4,n,t,b)
if m<=0:
    print(0,end='')
else:
    print(m,end='')   