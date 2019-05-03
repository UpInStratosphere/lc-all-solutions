class Solution(object):
  def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    #solution 1: first if loop check start pointer element until it is an alphabet, second if loop check end pointer element. when both ifs are satisfied, then we compare the two elements. If the same, we can move on the next one. Else, return false. Here, to check each pointer is a separate condition to be satisfied. 
    start, end = 0, len(s) - 1
    while start < end:
      if not s[start].isalnum():
        start += 1
        continue
      if not s[end].isalnum():
        end -= 1
        continue
      if s[start].lower() != s[end].lower():
        return False
      start += 1
      end -= 1
    return True
    
    
    #solution 2:
    l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
        return True
