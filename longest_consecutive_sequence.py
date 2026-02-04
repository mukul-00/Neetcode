# leetcode - 128 (google)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        if not nums:
            return 0

        nums = sorted(set(nums))

        current = 1
        longest = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current += 1
                longest = max(longest, current)
            else:
                current = 1
        
        return longest



if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]   

    sol = Solution()              
    result = sol.longestConsecutive(nums)

    print("Longest consecutive sequence length:", result)
