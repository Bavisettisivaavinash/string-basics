def check_anagrams(string1, string2):
    # check lengths of both the strings, if they are not equal return False.
    if len(string1) != len(string2):
        return False
    # def an empty dictionary
    char_counts = {}
    for char in string1:
        char_counts[char] = char_counts.get(char,0) + 1
    # now check string2, if letter is present decrease the count.
    for char in string2:
        if char not in char_counts or char_counts[char] == 0:
            return False
        char_counts[char] -= 1
    return True
str1="listen"
str2="silent"
if check_anagrams(str1,str2):
     print('anagrams!')
else:
    print('not anagrams!')