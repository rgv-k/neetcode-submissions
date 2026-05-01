class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int[] prefix = new int[n];
        int[] suffix = new int[n];
        suffix[n-1] = height[n-1];
        prefix[0] = height[0];
        for(int i =1; i < n; i++){
            prefix[i] = Math.max(height[i], prefix[i-1]);
            suffix[n-i-1] = Math.max(height[n-i-1],suffix[n-i]);
        }
        int total = 0;
        for(int i = 1; i < n-1;i++){
            total += (Math.min(prefix[i], suffix[i]) - height[i]);
        }

        return total;
    }
}
