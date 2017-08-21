# Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B 
# such that l ≤ A ≤ B ≤ r.

# Example

# For n = 6, l = 2 and r = 4, the output should be
# countSumOfTwoRepresentations2(n, l, r) = 2.

# There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4 and 6 = 3 + 3.

# Input/Output

# [time limit] 4000ms (py)
# [input] integer n

# A positive integer.

# Guaranteed constraints:
# 5 ≤ n ≤ 109.

# [input] integer l

# A positive integer.

# Guaranteed constraints:
# 1 ≤ l ≤ r.



def countSumOfTwoRepresentations2(n, l, r):
    count = 0
    for i in range(l, r + 1):
        if i <= n - i <= r and i <= (n-i):
            count += 1
    return count
