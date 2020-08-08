wt=[1,3,4,5]
val=[1,4,5,7]
w=7
n=4
dp=[[-1 for i in range(w+1)] for j in range(n+1)]
def knapsack(n,w):
    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif wt[i-1]<=j:
                dp[i][j]=max(val[i-1]+dp[i][j-wt[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    
    return dp[n][w]

print(knapsack(n, w))