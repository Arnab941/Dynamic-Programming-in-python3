a=list(map(int,input().split(',')))
x=len(a)
dp=[[-1 for i1 in range(x+1)]for i2 in range(x+1)]
def good(i,j,day):
    if i>j:
        return 0
    if dp[i+1][j+1]!=-1:
        return dp[i+1][j+1]
    else:
        dp[i+1][j+1]=max(((day*a[i])+good(i+1,j,(day+1))),((day*a[j])+good(i,j-1,(day+1))))
        return dp[i+1][j+1]         
m=good(0,x-1,1)
for i in dp:
    print(i)
print(m)