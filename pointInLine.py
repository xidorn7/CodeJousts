
# Check if the given point belongs to the given line.

# Example

# For point = [0, 1] and line = [1, 1, 0], the output should be
# pointInLine(point, line) = false;
# For point = [1, -1] and line = [1, 1, 0], the output should be
# pointInLine(point, line) = true.
# Check out the image below for better understanding:


# Solution 1

def pointInLine(point, line):
    m = line[1]/line[0]
    return line[1]-point[1] - m*(line[0] - point[0]) - line[2] == 0


# Solution 2

def pointInLine(point, line):
    return point[0]*line[0]+point[1]*line[1]+line[2]==0
