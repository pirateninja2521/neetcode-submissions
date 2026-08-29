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
    vector<int> preorderTraversal(TreeNode* root) {
        if (!root) return {};

        vector<int> values;
        values.push_back(root->val);
        vector<int> leftValues = preorderTraversal(root->left);
        vector<int> rightValues = preorderTraversal(root->right);
        values.insert(values.end(), leftValues.begin(), leftValues.end());
        values.insert(values.end(), rightValues.begin(), rightValues.end());
        return values;
    }
};