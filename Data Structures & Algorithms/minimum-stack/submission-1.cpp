class MinStack {
private:
    stack<int> normalStack, minStack;
public:
    MinStack() {}
    
    void push(int val) {
        normalStack.push(val);
        if (minStack.empty()) {
            minStack.push(val);
        }
        else {
            minStack.push(min(minStack.top(), val));
        }
    }
    
    void pop() {
        normalStack.pop();
        minStack.pop();
    }
    
    int top() {
        return normalStack.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};
