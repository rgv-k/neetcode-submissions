class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        List<List<Integer>> result = new ArrayList<>();
        for(int i = 0; i < n-2; i++){
            if(i > 0 && nums[i] == nums[i-1]) continue;
            int j = i+1;
            int k = n-1;
            while(j<k){
                int sum = nums[i] + nums[j] + nums[k];
                if(sum==0){
                    List<Integer> arr = new ArrayList<>();
                    arr.add(nums[i]);arr.add(nums[j]); arr.add(nums[k]);
                    j++;
                    k--;
                    while(nums[j] == nums[j-1] && j<k) j++;
                    while(nums[k] == nums[k+1] && j<k) k--;
                    result.add(arr);
                }
                else if(sum > 0) k--;
                else j++;
            }
        }

        return result;
    }
}
