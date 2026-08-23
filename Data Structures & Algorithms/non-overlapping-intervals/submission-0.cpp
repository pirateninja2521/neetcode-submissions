class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        int removeNum = 0;
        int prevEnd = intervals[0][1];
        for (int i = 1; i < intervals.size(); i++) {
            if (prevEnd <= intervals[i][0]) {
                prevEnd = intervals[i][1];
            }
            else { // Overlap
                removeNum++;
                if (intervals[i][1] <= prevEnd) {
                    prevEnd = intervals[i][1];
                }
                else {
                    continue;
                }
            }
        }
        return removeNum;
    }
};
