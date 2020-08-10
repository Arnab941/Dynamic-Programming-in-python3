x='12341'
y='341213'
m=len(x)
n=len(y)
dp=[[-1 for i in range(n+1)] for j in range(m+1)]
def lcs(m,n):
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif x[i-1]==y[j-1]:
                dp[i][j]=(1+dp[i-1][j-1])
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    
    i1=m
    j1=n
    c=''           
    while dp[i1][j1]!=0:
        if x[i1-1]==y[j1-1]:
            c+=(x[i1-1])
            i1-=1
            j1-=1
        else:
            if dp[i1-1][j1]>dp[i1][j1-1]:
                i1-=1
            else:
                j1-=1
                
    return c[::-1]

k=lcs(m,n)
print(k)