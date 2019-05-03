class Solution:
  # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
  # @return nothing
  def reverseWords(self, s):
    
    swap(0, len(s) - 1, s)
    
    wstart, wend = 0, 0
    for i in range(0, len(s)): #outer loop traversal pointer
      if s[i] == " ": #this means the word ended
        wend = i - 1 #word ended at the previous element (for words that do not end at the last element)
        swap(wstart, wend, s)
        wstart = i + 1 #assign the start of the new word. No need to worry about next two spaces being whitespace since the question said they are separated by one whitespace only.
      elif i + 1 == len(s): #for word that ended at the last element, the end should not be i - 1 but rather i itself)
        swap(wstart, i, s) 

    def swap(start, end, slist):  #reverse string function implementation
      while start < end:
        slist[start], slist[end] = slist[end], slist[start]
        start += 1
        end -= 1
