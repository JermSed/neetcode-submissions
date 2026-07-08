#include <set>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> checked;

        for(int i = 0; i < nums.size(); i++){
            if(checked.find(nums[i]) != checked.end()){
                return true;
            }
            checked.insert(nums[i]);
        }

        return false;

    }
};
