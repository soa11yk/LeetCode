class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, m = 0, {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9,"V": 5, "IV": 4, "I": 1}
        while s:
            i = 2 if s[:2] in m else 1
            n += m[s[:i]]
            s = s[i:]
        return n
