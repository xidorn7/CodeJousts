# Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

# Example

# For text = "Ready, steady, go!", the output should be
# longestWord(text) = "steady".


## Three great solutions using re

def longestWord(text):
    return sorted ((re.findall(r'\w+',text)), key = len, reverse = True)[0]


def longestWord(text):
    words = re.findall(r'\w+',text)
    return sorted ((w for w in words), key = len, reverse = True)[0] 

def longestWord(text):
    return sorted( re.findall('([a-zA-Z]*)',text), key=len )[-1]
