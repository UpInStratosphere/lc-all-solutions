bool isIsomorphic(string s, string t) {
        // create 2 different arrays to implement hashmap
        char map_s[128] = { 0 };
        char map_t[128] = { 0 };
        int len = s.size();
        // for each element in t and s string, if it can be found in map, increase its value by 1. otherwise, set it as 1. Because we are increasing the values, we should compare them the first thing next iteration to see if they are the same. NOT AFTER THE INCREASE IN VALUE FOR EACH CHAR.
        for (int i = 0; i < len; ++i)
        {
            if (map_s[s[i]]!=map_t[t[i]]) return false;
            map_s[s[i]] = i+1;
            map_t[t[i]] = i+1;
        }
        return true;    
    }
 
 
