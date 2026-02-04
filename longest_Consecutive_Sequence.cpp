#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
    //     if(nums.size() == 0) return 0;

    //     sort(nums.begin(), nums.end());

    //     int n = nums.size();

    //     int longest = 1;
    //     int lastSmaller = INT_MIN;
    //     int count = 0;

    //     for(int i = 0; i < n; i++){
    //         if(nums[i] - 1 == lastSmaller){
    //             count++;
    //             lastSmaller = nums[i];
    //         }
    //         else if (lastSmaller != nums[i]) {
    //             count = 1;
    //             lastSmaller = nums[i];
    //         }

    //         longest = max(longest, count);
    //     }

    //     return longest;
    // }

        int n = nums.size();

        if(n == 0) return 0;

        sort(nums.begin(), nums.end());

        int curr = 1;
        int mx = 1;

        for(int i = 1; i < n; i++){
            if(nums[i-1] == nums[i] - 1){
                curr++;
            }
            else if(nums[i-1] == nums[i]){
                // duplicate, skip
                continue;
            }
            else{
                curr = 1;
            }

            mx = max(mx, curr);
        }

        return mx;
    }
};  


int main() {

    vector<int> nums = {100, 4, 200, 1, 3, 2};

    Solution sol;

    int ans = sol.longestConsecutive(nums);

    cout << "Longest consecutive sequence length: " << ans << endl;

    return 0;
}
