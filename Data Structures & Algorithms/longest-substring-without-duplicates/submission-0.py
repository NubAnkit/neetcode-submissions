class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, ans = 0, 0, 0
        cur = set()
        while r < len(s):
            if s[r] not in cur:
                cur.add(s[r])
                r += 1
                if len(cur) > ans:
                    ans = len(cur)
            else:
                cur.remove(s[l])
                l += 1
        return ans