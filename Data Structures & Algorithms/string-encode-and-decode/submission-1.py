class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for cur in strs:
            size = len(cur)
            add = str(size) + "#" + cur
            word += add
        return word

    def decode(self, s: str) -> List[str]:
        current = 0
        size = ""
        sol = []
        while current < len(s):
            if s[current] != "#":
                size += s[current]
                current += 1
            else:
                current += 1 # to be at the first letter
                count = int(size)
                sol.append(s[current: current + count])
                current += count
                size = ""
        return sol
