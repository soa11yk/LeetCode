class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """ 
       
        count=0
        flag=0
        j=0
        
		##################for special occasions
        if len(strs)<1 or "" in strs: #if length of list of strs < 1 or empty in strs return empty
             return ""
        if len(strs)==1: #when length of list of string equals to 1, it returns the entire 0
            return strs[0]
        minlen=min(map(len,strs)) #map meaning applies a function to all items in a list
		###################check every string from 1 letter to the minlength of strings
        while True:
            cur=strs[0][j]
            for s in strs: #
                if cur!=s[j]:
                    flag=1
            if flag==1: #once be flagged, the loop breaks
                break
            else:
                count+=1
                j+=1
            if count==minlen: #if 
                break
        # if count==0:
        #     return ""
        # else:
        return strs[0][0:count]
