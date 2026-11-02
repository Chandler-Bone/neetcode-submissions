class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> check;
        
        for(auto& i : nums)
        {
            if(check.contains(i))
                return true;
            check.insert(i);
        }

        return false;
    }
};