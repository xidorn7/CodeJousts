# Given a permutation, produce its inverse permutation.

# Example

# For permutation = [1, 3, 4, 2], the output should be
# inversePermutation(permutation) = [1, 4, 2, 3].
# An inverse permutation is a permutation in which each number 
# and the number of the place which it occupies are exchanged.

# Solution 1

def inversePermutation(permutation):
    a = [0]*len(permutation)
    for i in range(len(permutation)):
        a[i] = permutation[permutation[i]-1]
    return a

# Soution 2

def inversePermutation(permutation):
    ret = [0]*len(permutation)
    
    for i,a in enumerate(permutation):
        ret[a-1] = i+1
    
    return ret
