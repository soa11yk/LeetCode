class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        prev_c = 0
        for c in s:
            if c == 'I':
                ret += 1
            elif c == 'V':
                if prev_c == 'I':
                    ret -= 1 
                    ret += 4
                else:
                    ret += 5
            elif c == 'X':
                if prev_c == 'I':
                    ret -= 1 
                    ret += 9
                else:
                    ret += 10
            elif c == 'L':
                if prev_c == 'X':
                    ret -= 10 
                    ret += 40
                else:
                    ret += 50
            elif c == 'C':
                if prev_c == 'X':
                    ret -= 10
                    ret += 90
                else:
                    ret += 100
            elif c == 'D':
                if prev_c == 'C':
                    ret -= 100
                    ret += 400
                else:
                    ret += 500
            elif c == 'M':
                if prev_c == 'C':
                    ret -= 100
                    ret += 900
                else:
                    ret += 1000
            else:
                raise Exception('wrong char encountered')
            
            prev_c = c
        return ret
