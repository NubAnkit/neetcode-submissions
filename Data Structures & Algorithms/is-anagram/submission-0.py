class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table = {}
        for i in s:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        for j in t:
            if j in table:
                table[j] -= 1
            else:
                table[j] = -1
        for value in table.values():
            if value != 0:
                return False
        return True