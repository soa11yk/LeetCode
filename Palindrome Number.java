class Solution {
    public boolean isPalindrome(int x) {
        int last_digit = 0;
        int reversedNum = 0;
        int input = x;
        
        while (x != 0) {    
            last_digit = x % 10;
                 
            reversedNum = reversedNum * 10 + last_digit;
            
            x = x / 10; 
        }
        
        if (input < 0) {
        return false;
        }
        else if (reversedNum == input) {
        return true;
        }
        else {
        return false;
        }    
        
    }
}
