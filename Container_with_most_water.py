class Solution:
    def maxArea(self, heights: list[int]) -> int:

        # BRUTE FORCE (O(n^2)) — try every pair
        # maxWater = 0
        # for i in range(len(heights)):
        #     for j in range(len(heights)):
        #         width = j - i
        #         height = min(heights[i], heights[j])
        #         area = width * height
        #         maxWater = max(maxWater, area)
        # return maxWater


        # OPTIMAL TWO POINTER APPROACH (O(n))

        maxWater = 0   # stores maximum area found

        l = 0                       # left pointer
        r = len(heights) - 1       # right pointer

        while l < r:

            width = r - l

            # Water level is limited by the shorter line
            height = min(heights[l], heights[r])

            area = width * height
            maxWater = max(maxWater, area)   # update answer

            # Move the pointer with smaller height
            # because taller side cannot increase area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxWater


if __name__ == "__main__":
    sol = Solution()

    heights = [1,7,2,5,4,7,3,6]

    result = sol.maxArea(heights)

    print(result)
