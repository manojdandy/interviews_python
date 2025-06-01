#W = 4, profit[] = [1, 2, 3], weight[] = [4, 5, 1]
# Output: 3

def kanpsack(W:int,profit:list,wt:list,n:int)->int:
    if W == 0 or n == 0:
        return 0
    elif wt[n-1] < W:
        return max(profit[n-1] + kanpsack(W-wt[n-1],profit,wt,n-1),
                   kanpsack(W,profit,wt,n-1))
    else:
        return kanpsack(W,profit,wt,n-1)


def kanpsack_with_dp(W:int,profit:list,wt:list,n:int,dp:list)->int:
    if W == 0 or n == 0:
        return 0
    if dp[n][W] != -1:
        return dp[n][W]
    elif wt[n-1] < W:
        dp[n][W] = max(profit[n-1] + kanpsack_with_dp(W-wt[n-1],profit,wt,n-1,dp),
                   kanpsack_with_dp(W,profit,wt,n-1,dp))
        return dp[n][W]
    else:
        dp[n][W] = kanpsack_with_dp(W,profit,wt,n-1,dp)
        return dp[n][W]



def kanpsack_with_matrix(W:int,profit:list,wt:list,i:int,j:int, dp:list)->int:
    """
    i range from 0 to profit
    j range from 0 to W 
    """
    pass
        

    
if __name__=="__main__":
    W = 4
    profit = [1, 2, 3]
    n = len(profit)
    print("*** calling ****")
    dp = [[-1 for _ in range(W+1)] for _ in range(n+1)]
    mt = dp
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j == 0 :
                mt[i][j] = 0

    print(f"size of dp :: {len(dp)}")
    res = kanpsack(W,[1, 2, 3],[4, 5, 1],n)
    print(res)

    res1 = kanpsack_with_dp(W,profit,[4, 5, 1],n,dp)
    print(res1)

    res2 = kanpsack_with_matrix(W,profit,[4, 5, 1],0,0,mt)
    print(res2)
