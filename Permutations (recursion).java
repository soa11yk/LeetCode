class Solution {
    
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        
        permuteRecursion(results, nums, 0, nums.length - 1);
        
        return results;
    }
    
    public void permuteRecursion(List<List<Integer>> results, int[] nums, int start, int end) {
        if(start == end) {
            List<Integer> result = new ArrayList<Integer>();
            for (int num : nums) {
                result.add(num);
            }
            results.add(result);
        } else {
            for(int i = start; i <= end; i++) {
                nums = swap(nums, start, i);
                permuteRecursion(results, nums, start + 1, end);
                nums = swap(nums, start, i);
            }
        }
    }
    
    public int[] swap(int[] nums, int first, int second) { //swap method to handle start & i
        int t = nums[first];
        nums[first] = nums[second];
        nums[second] = t;
        
        return nums;
    }
}
