class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int lo = 1;
        int hi = *max_element(piles.begin(), piles.end());
        
        int answer = hi;
        while(lo <= hi) {
            int mid = (lo + hi) / 2;
            if(canEatwithRate(mid, piles, h)) {
                answer = mid;
                hi = mid - 1;
            }
            else {
                lo = mid + 1;
            }
        }
        return answer;
    }

    bool canEatwithRate(int target, vector<int>& piles, int h) {
        int sum = 0;
        for (int pile : piles) {
            sum += (pile + target - 1) / target;
        }
        return sum <= h;
    }
};
