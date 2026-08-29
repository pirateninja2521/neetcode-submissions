/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        if (!root) return {};
        vector<int> values;
        vector<int> left_values = inorderTraversal(root->left);
        values.insert(values.end(),left_values.begin(), left_values.end());
        values.push_back(root->val);
        vector<int> right_values = inorderTraversal(root->right);
        values.insert(values.end(),right_values.begin(), right_values.end());
        return values;  
    }
};