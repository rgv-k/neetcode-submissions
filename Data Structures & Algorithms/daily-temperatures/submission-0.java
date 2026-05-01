class Solution {
    public int[] dailyTemperatures(int[] t) {
        Deque<int[]> stack = new ArrayDeque<>();
        int[] res = new int[t.length];
        for(int i =0; i < t.length; i++){
                while(!stack.isEmpty() && stack.peek()[0] < t[i]){
                    int[] a = stack.pop();
                    res[a[1]] = i-a[1];
                }
                stack.push(new int[]{t[i], i});
            }

        return res;
    }

}
