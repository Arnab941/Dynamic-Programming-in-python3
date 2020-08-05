a=[1,5,11,6]
n=len(a)
w1=sum(a)
w=w1//2
dp=[[-1 for i in range(w+1)] for j in range(n+1)]
def knapsack(n,w):
    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif a[i-1]<=j:
                dp[i][j]=max(a[i-1]+dp[i-1][j-a[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    
    return dp[n][w]

k=knapsack(n,w)
print(w1-(2*k)) 