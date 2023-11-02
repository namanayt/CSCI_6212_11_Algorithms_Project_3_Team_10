import sys
import time

# Algorithm to find the highest floor from which egg can be dropped without breaking
def find_first_drop(egg, fl):
    dp = [[0] * (fl + 1) for _ in range(egg + 1)]

    for i in range(1, fl + 1):
        dp[1][i] = i

    for i in range(2, egg + 1):
        for j in range(1, fl + 1):
            dp[i][j] = float('inf')
            low, high = 1, j
            while low <= high:
                mid = (low + high) // 2
                br_egg = dp[i - 1][mid - 1]
                no_br_egg= dp[i][j - mid]
                answer = 1 + max(br_egg, no_br_egg)
                dp[i][j] = min(dp[i][j], answer)
                if br_egg < no_br_egg:
                    low = mid + 1
                else:
                    high = mid - 1

    return low


m, n = 2, 20
sum = 0
counter = 500
res = 0
temp_counter = counter

while counter > 0:
    start_time = time.time_ns()
    res = find_first_drop(m, n)
    end_time = time.time_ns()
    sum  = sum + (end_time - start_time)
    counter -= 1

avg = sum / temp_counter
print("Initial floor from where egg can be dropped with", m, "eggs and", n, "floors is", res)
# print("Minimum number of trials in worst case with", n, "eggs and", k, "floors is", minTrials(n, k))
print("Time Taken: ", avg)
