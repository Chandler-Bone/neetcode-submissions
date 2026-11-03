class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::array<int, 26> count;
        std::unordered_map<string,vector<string>> umap;

        for(const auto& str : strs)
        {
            std::string hashkey;
            count.fill(0);

            for(const auto& c : str)
            {
                count[c - 'a']++;
            }
            // umap[hash_key].insert(str);
            for(const auto& i : count)
            {
                hashkey += "," + to_string(i);
            }
            // cout << hashkey;
            umap[hashkey].push_back(str);
        }

        vector<vector<std::string>> res;
        for(const auto& pair : umap)
        {
            res.push_back(pair.second);
        }
        return res;
    }
};
