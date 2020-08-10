x='abcdgh'
y='acdghr'
m=len(x)
n=len(y)
dp=[[-1 for i in range(n+1)] for j in range(m+1)]
def lcs(m,n):
    result=0
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif x[i-1]==y[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
                result=max(result,dp[i][j])
            else:
                dp[i][j]=0
                
    return result

k=lcs(m,n)
print(k) 