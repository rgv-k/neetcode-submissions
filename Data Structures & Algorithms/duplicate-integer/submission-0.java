class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> num = new HashSet<>();
        for(int i: nums){
            if(num.contains(i))  return true;

            else num.add(i);
        }

        return false;
    }
}