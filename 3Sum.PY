from itertools import permutations
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        l = list(permutations(nums, 3))
        l1 = list (l)
        # print (l1)
        
        lol = [list(elem) for elem in l1]
        
        i = 0
        while i < len(lol):
            if sum(lol[i]) == 0:
                res.append (lol[i])
                i+=1
                
            else:
                i+=1
                
        # ud = [list(x) for x in set(tuple(x) for x in res)]
        
        ud = [list(x) for x in set(tuple(x) for x in res)]
       
        
        print (res)
        print (ud)
   

            
            
     
        
        
        
