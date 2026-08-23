class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        sort(intervals.begin(), intervals.end());

        vector<int> sortedQueries = queries;
        sort(sortedQueries.begin(), sortedQueries.end());
        map<int, int> res;

        auto cmp = [](const vector<int>& a, const vector<int>& b) {
            int lenA = a[1] - a[0] + 1;
            int lenB = b[1] - b[0] + 1;
            if (lenA == lenB) return a[1] > b[1];
            return lenA > lenB;
        };
        priority_queue<vector<int>, vector<vector<int>>, decltype(cmp)> minHeap;

        int i = 0;

        for (int q : sortedQueries) {
            while (i < intervals.size() && intervals[i][0] <= q) {
                minHeap.push(intervals[i]);
                i++;
            }
            while (!minHeap.empty() && minHeap.top()[1] < q) {
                minHeap.pop();
            }

            res[q] = minHeap.empty() ? -1 : minHeap.top()[1] - minHeap.top()[0] + 1;
        }

        vector<int> result(queries.size());

        for (int j = 0; j < queries.size(); j++) {
            result[j] = res[queries[j]];
        }

        return result;
    }
};
