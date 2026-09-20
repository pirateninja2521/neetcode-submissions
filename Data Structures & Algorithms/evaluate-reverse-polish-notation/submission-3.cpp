class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        set<string> operators = {"+", "-", "*", "/"};
        stack<int> numbers;
        for (string token : tokens) {
            if (!operators.contains(token)) {
                int num = stoi(token);
                numbers.push(num);
                continue;
            }
            int n2 = numbers.top();
            numbers.pop();
            int n1 = numbers.top();
            numbers.pop();
            int result;
            switch (token[0]) {
                case '+': result = n1 + n2; break;
                case '-': result = n1 - n2; break;
                case '*': result = n1 * n2; break;
                case '/': result = n1 / n2; break;
            }
            numbers.push(result);
        }
        return numbers.top();
    }
};
