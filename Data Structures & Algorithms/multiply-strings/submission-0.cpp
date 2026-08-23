class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") return "0";

        int m = num1.size();
        int n = num2.size();

        vector<int> ans(m+n, 0);

        for (int i = m-1; i>=0; i--) {
            for (int j = n-1; j>=0; j--) {
                int mul = (num1[i] - '0') * (num2[j] - '0');
                int sum = mul + ans[i+j+1];

                ans[i + j + 1] = sum % 10;
                ans[i + j] += sum/10;
            }
        }
        string ret = "";
        int start = 0;
        while (start < ans.size() && ans[start] == 0) start++;
        while (start < ans.size()) {
            ret += to_string(ans[start]);
            start++;
        }
        return ret;
    }
};
