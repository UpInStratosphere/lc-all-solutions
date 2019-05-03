class Solution(object):
  def isOneEditDistance(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) >= len(t):
      i = 0
      while i < len(t) and s[i] == t[i]:
        i += 1
      return s != t and (s[i + 1:] == t[i:] if len(s) != len(t) else s[i + 1:] == t[i + 1:])
    else:
      return self.isOneEditDistance(t, s)

   
  
    #solution 2
    m = len(s1) 
    n = len(s2) 
  
    if abs(m - n) > 1: 
        return false 
  
    count = 0    
  
    i = 0
    j = 0
    while i < m and j < n: 
        if s1[i] != s2[j]: 
            if count == 1: 
                return false 
            
            if m > n: 
                i+=1
            elif m < n: 
                j+=1
                
            else:     
                i+=1
                j+=1
            
            count+=1
  
        else:   
            i+=1
            j+=1
  
    if i < m or j < n: 
        count+=1
  
    return count == 1
