class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length==0) return 0;
        int n = nums.length;
        HashSet<Integer> set1 = new HashSet<>();
        
        for(int i: nums) set1.add(i);

        int count=1;
        int max=0;

        for(Integer i: set1){
            if(!set1.contains(i-1)){
                count = 1;
                while(set1.contains(i+1)){
                    count++;
                    i++;
                }
            }
            max = Math.max(max, count);
        }

        return max;
    }
}
