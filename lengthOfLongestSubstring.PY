class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = [] #needs to resovle situation where longest substring starts in the middle
        ss2 = []
        i = 0
        i2 = len(s)-1
        l = list(s)
        for l[i] in l:
            if l[i] not in ss:
                ss.append (l[i])
                i +=1
        for l[i2] in l:
            if l[i2] not in ss2:
                ss2.append (l[i2])
                i2 -=1
        
        if len(ss) >= len(ss2):
            return (len(ss))
        else:
            return (ss2)


