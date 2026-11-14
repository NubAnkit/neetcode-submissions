class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = {}
        if len(strs) == 0: return [strs]
        for word in strs:
            current = [0] * 26
            for letter in word:
                number = ord(letter) - 97
                current[number] += 1
            tuple_current = tuple(current)
            if tuple_current in storage:
                storage[tuple_current].append(word)
            else:
                storage[tuple_current] = [word]
        return list(storage.values())
