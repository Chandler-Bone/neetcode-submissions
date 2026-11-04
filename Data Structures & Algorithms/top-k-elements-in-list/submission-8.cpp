class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> count;
        vector<set<int>> freq(nums.size() + 1);

        for(int i = 0; i < nums.size(); ++i)
        {
            count[nums[i]]++;
        }

        for(auto it = count.begin(); it != count.end(); ++it)
        {
            freq[it->second].insert(it->first);
        }

        vector<int> res;

        for(int i = freq.size() - 1; i > 0; --i)
        {
            if(res.size() == k)
                break;

            if(freq[i].empty())
                continue;
            
            for(auto e : freq[i])
            {
                if(res.size() == k)
                    break;
                res.emplace_back(e);
            }
        }

        return res;
    }
};
