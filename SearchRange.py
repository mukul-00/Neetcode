class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first():
            l = 0
            h = len(nums) - 1
            ans = -1 #target not found (if its found then store mid index)

            while(l <= h):
                mid = (l + h)//2

                guess = nums[mid]
                if(guess == target):
                    ans = mid
                    h = mid - 1 #move left
                elif(guess < target):
                    l = mid + 1
                else:
                    h = mid - 1
            return ans

        def last():
            l = 0
            h = len(nums) - 1
            ans = -1 #target not found

            while(l <= h):
                mid = (l + h)//2

                guess = nums[mid]
                if(guess == target):
                    ans = mid
                    l = mid + 1 #move right
                elif(guess < target):
                    l = mid + 1
                else:
                    h = mid - 1
            return ans

        return [first(), last()]

