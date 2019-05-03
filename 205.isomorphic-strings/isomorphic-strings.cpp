bool isIsomorphic(string s, string t) {
        // create 2 different arrays to implement hashmap of each chars implicitly.
        char map_s[128] = { 0 };
        char map_t[128] = { 0 };
        int len = s.size();
        // for each element in t and s string, indirectly map them to a number (which will be used as the index for both arrays). Each index of the new array will be a numberical mapping of each letter in each string and its value will be the number of times it appeared. 
        for (int i = 0; i < len; ++i)
        {
            if (map_s[s[i]]!=map_t[t[i]]) return false;
            map_s[s[i]] = i+1;
            map_t[t[i]] = i+1;
        }
        return true;    
    }
 
 
