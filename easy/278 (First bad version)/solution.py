# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        ans = 1
        while(l <= r):
            mid = int(l + (r - l) / 2)
            if(isBadVersion(mid)):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans