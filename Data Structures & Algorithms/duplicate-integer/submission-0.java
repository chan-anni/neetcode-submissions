class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> noDupe = new HashSet<Integer>();
        for(int num : nums) {
            if (noDupe.contains(num)) {
                return true;
            }
            noDupe.add(num);
        }
        return false;
    }
}