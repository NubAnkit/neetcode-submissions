class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = {}
        if len(strs) == 0: return [strs]
        for word in strs:
            current = (0, ) * 26
            for letter in word:
                number = ord(letter) - 97
                current = current[:number] + (current[number] + 1,) + current[number + 1:]
            if current in storage:
                storage[current].append(word)
            else:
                storage[current] = [word]
        return list(storage.values())
