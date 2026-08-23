class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> updatedIntervals;
        for(const auto& interval : intervals) {
            if (interval[1] < newInterval[0]) {
                updatedIntervals.push_back(interval);
            }
            else if (newInterval[1] < interval[0]) {
                updatedIntervals.push_back(newInterval);
                newInterval = interval;
            }
            else {
                newInterval = {min(newInterval[0], interval[0]), max(newInterval[1], interval[1])};
            }
        }
        updatedIntervals.push_back(newInterval);
        return updatedIntervals;
    }
};
