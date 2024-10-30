def unique_ways_recursive(n, m):
    if n == 0 or m == 0:
        return 1

    if n == 1 or m == 1:
        return 1

    return unique_ways_recursive(n -1, m) + unique_ways_recursive(n, m-1)

def unique_ways_memoized(n, m, cache=None):
    if cache is None:
        cache = {}

    if n == 1 or m == 1:
        return 1

    if (n,m) in cache:
        return cache[(n,m)]

    cache[(n,m)] = unique_ways_recursive(n -1, m, cache) + unique_ways_recursive(n, m - 1, cache)  

    return cache[(n,m)]

def unique_paths_dp(n, m):
    dp = [[1 for _ in range(m)] for _ in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[n - 1][m - 1]

def dp_fibonacci_recursive(n):
    if n == 0:
        return

    if n == 1:
        return 1

    return dp_fibonacci_recursive(n - 1), dp_fibonacci_recursive(n - 2)

def dp_fibonacci_memoized(n, cache=None):
    if n == 0:
        return 0

    if n == 1:
        return 1

    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]

    cache[n] = dp_fibonacci_memoized(n - 1, cache) + dp_fibonacci_memoized(n - 2, cache)

    return cache[n]
   
def dp_fibonacci_bottom_up(n):
    dp = [-1] * (n +1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

def coin_change_recursive(coins: list, amount: int):
    if amount == 0:
        return 1

    if amount < 0:
        return 0

    if len(coins) == 0:
        return 0

    return coin_change_recursive(coins, amount - coins[0]) + coin_change_recursive(coins[1:], amount)

def coin_change_memoized(coins: list, amount: int, cache=None):
    if cache is None:
        cache = {}

    if len(coins) == 0:
        return 0

    if amount == 0:
        return 1

    if amount < 0:
        return 0

    key = (amount, tuple(coins))
    if key in cache:
        return cache[key]

    cache[key] = coin_change_memoized(coins, amount - coins[0]) + coin_change_memoized(coins[1:], amount)
    return cache[key]

def coin_change_bottom_up(coins: list, amount: int):
    dp = [0] * (amount + 1)
    dp[0] = 1

    