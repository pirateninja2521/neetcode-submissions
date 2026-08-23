/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), [](Interval a, Interval b){
            if (a.start == b.start) return a.end < b.end;
            return a.start < b.start;
        });

        priority_queue<int, vector<int>, greater<int>> meetingRooms;
        for (auto& interval: intervals) {
            if (!meetingRooms.empty() && interval.start >= meetingRooms.top()){
            meetingRooms.pop();
            }
            meetingRooms.push(interval.end);
        }
        return meetingRooms.size();
    }
};
