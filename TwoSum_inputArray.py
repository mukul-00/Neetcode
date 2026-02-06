class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        left = 0
        right = len(nums) - 1

        # loop until both pointers meet
        while left < right:
            # calculate sum of elements at left and right
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                return [left+1, right+1]

            
            elif current_sum > target:
                right -= 1
    
            else:
                left += 1


nums = [2, 3, 5, 8]
target = 10

solution = Solution()
print(solution.twoSum(nums, target))
