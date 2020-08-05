wt=[2,3,7,8,10]
w=11
n=5
dp=[[-1 for i in range(w+1)] for j in range(n+1)]
def subset_sum(n,w):
    for i in range(n+1):
        for j in range(w+1):
            if j==0:
                dp[i][j]=True
            elif i==0:
                dp[i][j]=False
            elif wt[i-1]<=j:
                dp[i][j]=(dp[i-1][j-wt[i-1]] or dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]

    return dp[n][w]

print(subset_sum(n, w)) 