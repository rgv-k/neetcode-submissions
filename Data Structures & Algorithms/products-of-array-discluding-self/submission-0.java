class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] p = new int[nums.length];
        int[] s = new int[nums.length];
        int[] r = new int[nums.length];
        p[0]=nums[0];
        s[nums.length-1] = nums[nums.length-1];
        for(int i = 1; i < nums.length; i++){
            p[i] = p[i-1]*nums[i];
            s[nums.length-i-1] = s[nums.length-i]*nums[nums.length-i-1];
        }

        r[0] = s[1];
        r[nums.length-1] = p[nums.length-2];
        for(int i=1;i < nums.length-1;i++){
            r[i] = p[i-1]*s[i+1];
        }
        return r;
    }
}  
