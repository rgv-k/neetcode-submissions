class Solution {
    public int search(int[] nums, int target) {
        int i = 0;
        int n = nums.length;
        int j = n-1;
        int mid = (j+i)/2;
        while(i<=j){
            mid = (j+i)/2;
            if(target==nums[mid]) return mid;
            else if(target > nums[mid]) i = mid+1;
            else j = mid-1;
        }

        return -1;
    }
}
