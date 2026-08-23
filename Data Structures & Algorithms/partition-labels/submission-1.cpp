class Solution {
public:
    vector<int> partitionLabels(string s) {
        unordered_map<char, int> lastIndex;

        for (int i = 0; i < s.length(); i++) {
            lastIndex[s[i]] = i;
        }

        vector<int> partitions;
        int current_length = 0, partition_end = 0;
        for (int i = 0; i < s.length(); i++) {
            current_length += 1;
            partition_end = max(partition_end, lastIndex[s[i]]);

            if (i == partition_end) {
                partitions.push_back(current_length);
                current_length = 0;
            }
        }
        return partitions;
    }
};
