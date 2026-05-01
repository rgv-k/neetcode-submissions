class MinStack {
    ArrayList<Integer> stack1;
    ArrayList<Integer> stack2;
    int top = -1;
    public MinStack() {
        stack1 = new ArrayList<>();
        stack2 = new ArrayList<>();
    }
    
    public void push(int val) {
        stack1.add(val);
        if(top==-1) stack2.add(val);
        else stack2.add(Math.min(val, stack2.get(top)));
        top++;
    }
    
    public void pop() {
        stack1.remove(top);
        stack2.remove(top);
        top--;
    }
    
    public int top() {
        return stack1.get(top);
    }
    
    public int getMin() {
        return stack2.get(top);
    }
}
