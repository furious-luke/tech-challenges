#include <iostream>
#include <vector>
#include <unordered_map>
#include <cassert>

using namespace std;

class Solution {
public:
  vector<int>
  twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> delta_map;
    for (int ii = 0; ii < nums.size(); ++ii) {
      const int value = nums[ii];
      const auto other_index_it = delta_map.find(value);
      if (other_index_it != delta_map.end()) {
        return vector<int>{ii, other_index_it->second};
      }
      delta_map[target - value] = ii;
    }
    return vector<int>();
  }
};

int main(int argc, char* argv[]) {
  {
    vector<int> nums{2, 7, 11, 15};
    int target = 9;
    auto result = Solution().twoSum(nums, target);
    for (const auto ii : result) {
      cout << ii << " ";
    }
    cout << endl;
  }
  return 0;
}
