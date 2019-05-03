class Solution(object):
  def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
  #solution 1 time: O(s + t) space: O(s)
  def isAnagram1(self, s, t):
    if len(s) != len(t) return false
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
    
    for item in t:
        if item in dict1:
          dic1[item] = dic1.get(item, 0) - 1
          if dic1[item] < 0 return false
        else:
          return false
    
    return true
   
  #solution 2
  def isAnagram2(self, s, t):
    #create an array that uses each index as a sub for each alphabet. since 'a' would be at 0, we use the distance to determine the index of the char in the array. 
    dic1 = [0]*26
    for item in s:
        dic1[ord(item)-ord('a')] += 1
   
    for item in t:
        if item in dict1:
          dic1[item] = dic1.get(item, 0) - 1
          if dic1[item] < 0 return false
        else:
          return false
    
    return true
