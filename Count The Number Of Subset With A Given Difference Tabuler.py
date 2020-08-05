'''can be use as Target sum'''

a=[1,1,2,3]
sa=sum(a)
diff=1
w=(sa+diff)//2
n=len(a)
dp=[[-1 for i in range(w+1)] for j in range(n+1)]
def count_subset_sum(n,w):
    for i in range(n+1):
        for j in range(w+1):
            if j==0:
                dp[i][j]=1
            elif i==0:
                dp[i][j]=0
            elif a[i-1]<=j:
                dp[i][j]=(dp[i-1][j-a[i-1]] + dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]

    return dp[n][w]

print(count_subset_sum(n, w))