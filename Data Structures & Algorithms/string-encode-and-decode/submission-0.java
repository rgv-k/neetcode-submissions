class Solution {

    public String encode(List<String> strs) {
        StringBuilder str = new StringBuilder();
        for(String s: strs){
            str.append(s.length());
            str.append('#');
            str.append(s);
        }

        return str.toString();
    }

    public List<String> decode(String str) {
        String s = str;
        List<String> strs = new ArrayList<>();
        int i = 0;
        while(i < s.length()){
            int delimiter = s.indexOf("#", i);
            int len = Integer.parseInt(s.substring(i, delimiter));
            i = delimiter + 1;
            String sub = s.substring(i, i+len);
            strs.add(sub);
            i += len;
        }

        return strs;
    }
}