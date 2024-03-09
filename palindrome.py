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