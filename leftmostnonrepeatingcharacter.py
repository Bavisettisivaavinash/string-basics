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

# left most non repeating character index 'using hashing'
def leftmostnonrepeating(string):
    x = list(string)
    my_dict = {}
    for i in x:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    for j in x:
        if my_dict[j] == 1:
            return j
    return -1
text = input("enter string: ")
leftmostnonrepeating(text)