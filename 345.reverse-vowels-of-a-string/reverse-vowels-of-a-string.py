import string


class Solution(object):
  def reverseVowels(self, s):
    """
    :type s: str
    :rtype: str
    """
    vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]) #turn a list of strings into a set to have O(1) search time
    s = list(s) #turn the given string into a list. otherwise, everytime swapping would make a new string. this is an optimization
    start, end = 0, len(s) - 1
    while start < end:
      if s[start] not in vowels:
        start += 1
      elif s[end] not in vowels:
        end -= 1
      else:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return "".join(s) #turn the modified list into the answer string
