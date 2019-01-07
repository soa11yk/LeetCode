class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        s_list = list(s)
        c_list = []
        for i in range(len(s)):
            c_char = s_list[i]
            if c_char in c_list:
                c_list = c_list[c_list.index(c_char)+1:len(c_list)] #if current char is in c_list, then c_list is replaced by a new substring starting from the next char of the string to the end of the string
            c_list.append(c_char)
            if len(c_list) > longest:
                longest = len(c_list)
        return longest
      
