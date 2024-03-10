# left most non repeating character index
def leftmostnonrepeating(string):
    for i in range(len(string)):
        count = 0
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                count = count + 1
        if count == 0:
            return i
    return -1
text = input("enter string: ")
leftmostnonrepeating(text)