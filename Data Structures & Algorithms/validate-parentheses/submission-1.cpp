class Solution {
public:
    bool isValid(string s) {
        stack<char> openBrackets;
        for (char c:s) {
            switch (c) {
                case '[':
                case '{':
                case '(':
                    openBrackets.push(c);
                    continue;
                case ']':
                    if (openBrackets.empty() || openBrackets.top() != '[') return false;
                    break;
                case ')':
                    if (openBrackets.empty() || openBrackets.top() != '(') return false;
                    break;
                case '}':
                    if (openBrackets.empty() || openBrackets.top() != '{') return false;
                    break;
            }
            openBrackets.pop();
        }
        return openBrackets.empty();
    }
};
