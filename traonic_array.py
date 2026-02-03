class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        n = len(nums)
        phase = 0

        for i in range(1, n):

            if phase == 0 and nums[i] > nums[i - 1]:
                phase = 1
                continue

            if phase == 1 and nums[i] < nums[i - 1]:
                phase = 2
                continue

            if phase == 2 and nums[i] > nums[i - 1]:
                phase = 3
                continue

            

            if phase == 0 and nums[i] <= nums[i - 1]:
                return False

            if phase == 1 and nums[i] <= nums[i - 1]:
                return False

            if phase == 2 and nums[i] >= nums[i - 1]:
                return False

            if phase == 3 and nums[i] <= nums[i - 1]:
                return False

        return phase == 3


def main():
    nums = [1, 4, 6, 3, 2, 5, 9]   

    obj = Solution()
    result = obj.isTrionic(nums)

    if result:
        print("Trionic Array ")
    else:
        print("Not Trionic ")


if __name__ == "__main__":
    main()
