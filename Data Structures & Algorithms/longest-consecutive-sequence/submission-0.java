class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0) return 0;
        int[] num = Arrays.stream(nums).distinct().sorted().toArray();
        int count = 1;
        int result = 1;
        int i = 0;
        while(i < num.length - 1){
            if(num[i+1] == num[i] + 1){
                count++;
                i++;
            }
            else{
                result = result > count ? result : count;
                count = 1;
                i++;
            }
        }
        result = result > count ? result : count;

        return result;
    }
    
}
