def is_palindrome(text):
  """Checks if a string is a palindrome using two pointers, without preprocessing."""
  left, right = 0, len(text) - 1
  while left < right:
    # Skip non-alphanumeric characters on the left
    while left < right and not text[left].isalnum():
        left += 1

    # Skip non-alphanumeric characters on the right    
    while left < right and not text[right].isalnum():
        right -= 1

    # Compare characters (case-insensitive)
    if text[left].lower() != text[right].lower():
        return False

    # Move pointers inward
    left += 1
    right -= 1

  return True  # It's a palindrome!

# Example usage
test_string = "A man, a plan, a canal: Panama!"
if is_palindrome(test_string):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
