class Solution(object):
  def isIsomorphic(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
    
    # another solution: time: O(n), space is O(256) 
    d1, d2 = {}, {}
    #create a hashmap to store the number of occurences of each char in the string for both strings. 
    #sort the hashmaps by values and compare the sorted values. 
    for i, val in enumerate(s):
        d1[val] = d1.get(val, []) + [i]
    for i, val in enumerate(t):
        d2[val] = d2.get(val, []) + [i]
    return sorted(d1.values()) == sorted(d2.values())
    
    #another solution
    d1, d2 = [[] for _ in range(256)], [[] for _ in range(256)]
    for i, val in enumerate(s):
        d1[ord(val)].append(i)
    for i, val in enumerate(t):
        d2[ord(val)].append(i)
    return sorted(d1) == sorted(d2)
  
