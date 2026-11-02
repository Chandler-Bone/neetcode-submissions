class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> check;

        for(int i = 0; i < nums.size(); i++)
        {
            int diff = target - nums[i];
            auto it = check.find(diff);
            if(it != check.end())
                return vector<int> {it->second, i};

            check[nums[i]] = i;
        }
        return vector<int> {-1, -1};
    }
};
