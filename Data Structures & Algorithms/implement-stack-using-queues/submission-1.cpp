class MyStack {
private:
    array<queue<int>, 2> queues;
    int current = 0;
    int last = -1;

public:
    MyStack() {
        
    }
    
    void push(int x) {
        queues[current].push(x);
        last = x;
    }
    
    int pop() {
        int other = 1 - current;
        while (queues[current].size() > 1) {
            int num = queues[current].front();
            queues[current].pop();
            queues[other].push(num);

            last = num;
        }
        int ans = queues[current].front();
        queues[current].pop();

        current = other;
        return ans;
    }
    
    int top() {
        return last;
    }
    
    bool empty() {
        return queues[current].empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */