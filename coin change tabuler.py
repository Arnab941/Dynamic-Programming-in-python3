coin=[1,2,3]
n=3
sums=5
dp=[[-1 for i in range(sums+1)] for j in range(n+1)]
def coin_change(n,sums):
    for i in range(n+1):
        for j in range(sums+1):
            if j==0:
                dp[i][j]=1
            elif i==0:
                dp[i][j]=0
            else:
                if coin[i-1]<=j:
                    dp[i][j]=dp[i][j-coin[i-1]]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
                    
    return dp[n][sums]

print(coin_change(n, sums))