def reverse(string):
    revstring=""
    for i in range(len(string)-1,-1,-1):
        revstring += string[i]
    return revstring
print(reverse("avinash"))