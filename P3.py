import random
import time

def min_cost(n, k, a, c):
    # Create a 2D Dynamic Programming matrix to store the minimum cost
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]

    for j in range(k + 1):
        dp[1][j] = 0

    # Loop through galaxies and astro-haunted galaxies
    for i in range(2, n + 1):
        for j in range(1, k + 1):
            if a[i] == 1:
                for i_prime in range(1, n + 1):
                    if a[i_prime] == 1:
                        dp[i][j] = min(dp[i][j], dp[i_prime][j - 1] + c[i_prime][i])

    # Update the cost in a variable
    min_cost1 = dp[n][k]
    return min_cost1

a = [0]  # Ensure the first element is 0
n = int(input())  # number of galaxies
k = int(input())  # maximum number of astro-haunted galaxies allowed


# Initialize the c - matrix as a list of lists
c = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(n + 1):
    a.append(random.randint(0, 1))

a[-1] = 0  # Ensure the last element is 0

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        c[i][j] = random.randint(1, 10)  # Ensure non-zero cost

start = time.time_ns() # timer start
min_cost = min_cost(n, k, a, c)
print("Minimum cost to reach the galaxy", n, "with at most", k, "astro-haunted galaxies is:", min_cost)
print(a)
end = time.time_ns()
print(end - start)