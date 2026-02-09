class Solution:
    def mySqrt(self, x: int) -> int:

        # Handle small cases
        if x < 2:
            return x
            
        l = 1
        r = x // 2

        # Binary search for floor(sqrt(x))
        while l <= r:
            mid = (l + r) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                l = mid + 1
            else:
                r = mid - 1

        # r will be the floor value of sqrt(x)
        return r


if __name__ == "__main__":
    sol = Solution()

    test_cases = [0, 1, 4, 8, 10, 16, 26]

    for x in test_cases:
        print(f"sqrt({x}) = {sol.mySqrt(x)}")
