def popcount(n,bittocount):
    ans = 0
    while n != 0:
        ans += ~(n^bittocount)
        n >>= 1
    return ans
def bit(n,ind):
    return (n >> ind) & 1
def first(n):
    ans = 0
    if n == 0: return None
    while n != 0:
        if (n&1):
            return ans
        n >>= 1
        ans += 1
    return ans
def hamiltonianPath(adjList):
    #! https://www.geeksforgeeks.org/hamiltonian-path-using-dynamic-programming/
    n = len(adjList)
    # print(n)
    dp = [[0 for i in range(1<<n)] for j in range(n)]
    # print(dp)
    for i in range(n):
        dp[i][1<<i] = 1
    for i in range(1<<n):
        for j in range(n):
            if bit(i,j):
                for k in range(n):
                    if (bit(i,k) and j in adjList[k] and dp[k][i ^ (1<<j)]):
                        dp[j][i] = 1
                        break
    for i in range(n):
        if dp[i][(1<<n) - 1]:
            return True
    return False

