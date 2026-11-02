class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length())
            return false;
        
        int char_count [26];
        for(int i = 0; i < s.length(); i++)
        {
            char_count[int(s[i]) - int(char('a'))] += 1;
            char_count[int(t[i]) - int(char('a'))] -= 1;
        }

        for(int i = 0; i < 26; i++)
        {
            if(char_count[i] != 0)
                return false;
        }

        return true;
        
    }
};
