class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = [] #needs to resovle situation where longest substring starts in the middle
        ss2 = []
        i = 0
        l = list(s)
        
        for l[i] in l:
            if l[i] not in ss:
                ss.append (l[i])
                i +=1
        
        t = i-1
        print (t)
            
        for l[t] in l:
            if l[t] not in ss2:
                ss2.append (l[t])
                t+=1
          
                
                
        if len(ss) >= len(ss2):
            return len(ss)
        if len(ss) < len(ss2):
            return len(ss2)
        else:
            return len(s)
