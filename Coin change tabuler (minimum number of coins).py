coin=[1,2,3]
n=3
sums=7
dp=[[-1 for i in range(sums+1)] for j in range(n+1)]
def coin_change(n,sums):
    for i in range(n+1):
        for j in range(sums+1):
            if i==0:
                dp[i][j]=10**10
            elif j==0:
                dp[i][j]=0
            elif i==1:
                if j%coin[0]==0:
                    dp[i][j]= j//coin[0]
                else:
                    dp[i][j]=10**10
            else:
                if coin[i-1]<=j:
                    dp[i][j]=min(1+dp[i][j-coin[i-1]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
                    
    return dp[n][sums]

print(coin_change(n, sums))