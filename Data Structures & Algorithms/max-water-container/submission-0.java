class Solution {
    public int maxArea(int[] heights) {
        int n = heights.length;
        int i = 0;
        int j = n - 1;
        int result = 0;
        while(i < j){
            int temp = (j-i)*Math.min(heights[i], heights[j]);
            if(temp > result) result= temp;
            if(heights[i] > heights[j]) j--;
            else i++;
        }
        return result;
    }
}
