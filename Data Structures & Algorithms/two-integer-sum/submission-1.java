class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> diff = new HashMap<>();
        // difference, 
        for (int i = 0; i < nums.length; i++) {
            diff.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++) {
            int difference = target - nums[i];
            if (diff.containsKey(difference) && diff.get(difference) != i) {
                return new int[] {i, diff.get(difference)};
            }
        }
        return new int[0];
    }
}
