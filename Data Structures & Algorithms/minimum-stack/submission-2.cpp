class MinStack {
private:
    stack<pair<int, int>> minStack;
public:
    MinStack() {}
    
    void push(int val) {
        int minVal = minStack.empty() ? val : min(minStack.top().second, val);
        minStack.push(make_pair(val, minVal));
    }
    
    void pop() {
        minStack.pop();
    }
    
    int top() {
        return minStack.top().first;
    }
    
    int getMin() {
        return minStack.top().second;
    }
};
