# two pointer method
def is_palindrome(word):
  left, right = 0, len(word) - 1
  while left < right:
    if word[left] != word[right]:
      return False
    left += 1
    right -= 1
  return True
if is_palindrome("racecar"):
  print("palindrome!")
else:
  print("not palindrome!")


# using python builtin functions
def palindrome():
    text = input("enter string: ")
    result = text[::-1]
    if text == result:
        return True
    else:
        return False
palindrome()