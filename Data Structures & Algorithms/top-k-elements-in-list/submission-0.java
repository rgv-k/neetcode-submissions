class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i: nums){
            if(!map.containsKey(i)) map.put(i, 1);
            else map.put(i, map.get(i)+1);
        }

        List<Integer>[] bkt = new List[nums.length+1];

        for(int key: map.keySet()){
            int v = map.get(key);
            if(bkt[v]==null) bkt[v] = new ArrayList<>();
            bkt[v].add(key); 
        }

        List<Integer> result = new ArrayList<>();
        for(int i = bkt.length-1; (i >=0)&&(k>0); i--){
            if(bkt[i]!=null){
                for(int val: bkt[i]){
                    if(k!=0){
                    result.add(val);
                    k--;
                    }
                    else break;
                    
                }
            }
        }
        int[] resArr = new int[result.size()];
        for(int i = 0; i < result.size(); i++) resArr[i] = result.get(i);
        return resArr;
    }
}