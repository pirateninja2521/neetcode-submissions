class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        vector<int> temp(nums.size());
        mergeSort(nums, temp, 0, nums.size()-1);
        return nums;
    }

private:
    void mergeSort(vector<int>& nums, vector<int>& temp, int start, int end) {
        if (start >= end) {
            return;
        }
        int mid = start + (end - start) / 2;

        mergeSort(nums, temp, start, mid);
        mergeSort(nums, temp, mid+1, end);

        int pointer1 = start, pointer2 = mid+1;
        int pointer3 = start;
        while (pointer1 <= mid || pointer2 <= end) {
            if (pointer2 > end || (pointer1 <= mid && nums[pointer1] < nums[pointer2])) {
                temp[pointer3++] = nums[pointer1++]; 
            }
            else {
                temp[pointer3++] = nums[pointer2++];
            }
        }

        for(int i = start; i <= end; i++) {
            nums[i] = temp[i];
        }
    }
};