class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {  // start from i+1 to avoid comparing same elements
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};  // return indices of the two elements
                }
            }
        }
        return new int[0];  // return empty array if no result (edge case)
    }
}
