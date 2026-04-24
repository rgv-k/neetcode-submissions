class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        String str = s.replaceAll("[^a-z0-9]", "");
        char[] c = str.toCharArray();


        int i =0;
        int j = c.length-1;
        while(i<j){
            if(c[i]!=c[j]) return false;
            else{
                i++; j--;
            }
        }
        return true;
    }
}
