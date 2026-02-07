class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()              # sort array first
        l = []                   # list to store answers
        n = len(nums)

        for i in range(n):      # first number loop

            # skip duplicate first elements
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1           # second pointer
            k = len(nums) - 1  # third pointer (from end)

            target = -nums[i]  # we want nums[j] + nums[k] = target

            while(j < k):

                # found valid triplet
                if(nums[j] + nums[k] == target):
                    l.append([ nums[i], nums[j], nums[k]])

                    j = j + 1   # move both pointers
                    k = k - 1

                    # skip duplicate j values
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                # sum too small → move j right
                elif (nums[j] + nums[k] < target):
                    j = j + 1
                
                # sum too large → move k left
                else:
                    k = k - 1

        return l                # return all triplets


if __name__ == "__main__":
    sol = Solution()

    nums = [-1,0,1,2,-1,-4]

    result = sol.threeSum(nums)

    print(result)
