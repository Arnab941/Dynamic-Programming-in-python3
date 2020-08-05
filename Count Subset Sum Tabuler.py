wt=[2,3,5,6,8,10]
w=10
n=6
dp=[[-1 for i in range(w+1)] for j in range(n+1)]
def count_subset_sum(n,w):
    for i in range(n+1):
        for j in range(w+1):
            if j==0:
                dp[i][j]=1
            elif i==0:
                dp[i][j]=0
            elif wt[i-1]<=j:
                dp[i][j]=(dp[i-1][j-wt[i-1]] + dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]

    return dp[n][w]

print(count_subset_sum(n, w))