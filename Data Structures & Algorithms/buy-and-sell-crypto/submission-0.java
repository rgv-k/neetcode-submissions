class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int profit = 0;
        int n = prices.length;
        int[] pref = new int[n];
        pref[0] = prices[0];
        for(int i = 1; i < n;i++){
            pref[i] = Math.min(prices[i], pref[i-1]);
        }

        for(int i = 1;i < n; i++){
            profit = prices[i]-pref[i];
            max = Math.max(max, profit);
        }

        return max;
    }
}
