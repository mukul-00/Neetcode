class Solution:
    def solve(self, nums, ans, index):
        # base case
        if(index >= len(nums)):
            ans.append(nums[:])
            return 
        
        for j in range(index, len(nums)):
            nums[index], nums[j] = nums[j], nums[index]
            self.solve(nums, ans, index + 1)
            #backtracking -> baar baar same lekar aa rha haai 
            nums[index], nums[j] = nums[j], nums[index]


    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        index = 0
        self.solve(nums, ans, index)
        return ans