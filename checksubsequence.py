# check if a string is subsequence of the other
def subsequence(mainstr,substr):
    i=0
    j=0
    while i < len(mainstr) and j < len(substr):
            if mainstr[i] == substr[j]:
                i=i+1
                j=j+1
            i = i+1
    if j != len(substr):
        return False
    return True
str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
subsequence(str1, str2)