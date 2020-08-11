x='ytn'
y='sayantan'
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
                
    return dp[m][n]

k=lcs(m,n)
if k==m:
    print('True')
else:
    print('False') 