class Solution {
    public boolean isValid(String s) {
        if(s==null) return false; 
        Deque<Character> stack = new ArrayDeque<>();
        char[] ar = s.toCharArray();
        for(char c: ar){
            if(c=='('||c=='{'||c=='[') stack.push(c);
            else{
                if(stack.isEmpty()) return false;
                if(c==')'&&stack.peek()=='(') stack.pop();
                else if(c==']'&&stack.peek()=='[') stack.pop();
                else if(c=='}'&&stack.peek()=='{') stack.pop();
                else return false;
            }

        }
        return stack.isEmpty();
    }
}
