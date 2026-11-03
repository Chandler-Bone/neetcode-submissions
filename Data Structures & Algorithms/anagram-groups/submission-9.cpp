class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> umap;

        for(const auto str : strs)
        {
            int count[26] = {};
            string hashkey;

            for(const auto c : str)
            {
                count[c - 'a']++;
            }

            for(const auto i : count)
            {
                hashkey += "," + to_string(i);
            }

            umap[hashkey].emplace_back(str);
        }

        vector<vector<string>> res;
        for(auto it = umap.begin(); it != umap.end(); ++it)
        {
            res.emplace_back(it->second);
        }

        return res;
    }
};
