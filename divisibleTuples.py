# Given array of integers, find the number of sorted pairs formed by its (different) elements such that 
# the second element in the pair is divisible by the first one.

# Example

# For sequence = [1, 3, 2], the output should be
# divisorsPairs(sequence) = 2.

# These pairs are: (1, 3), (1, 2).

# For sequence = [2, 4, 8], the output should be
# divisorsPairs(sequence) = 3.

# These pairs are: (2, 4), (2, 8), (4, 8).

def divisorsPairs(sequence):
    count = 0
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            if sequence[j] % sequence[i] == 0:
                count += 1
    return count

### Less optimal 
def divisorsPairs(sequence):
    count = 0
    for i in range(len(sequence)):
        for j in range(len(sequence)):
            if sequence[i] % sequence[j] == 0 and i != j:
                count += 1
    return count
