class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        inv_store = {}
        ans = []
        left = 0;
        if len(nums) == 1:
            return nums
        for i in nums:
            if i in store:
                store[i] += 1
            else:
                store[i] = 1
        for j in store:
            if store[j] in inv_store:
                inv_store[store[j]].append(j)
            else:
                inv_store.setdefault(store[j], []).append(j)
        for i in range(len(nums), 0, -1):
            left = k - len(ans)
            if left == 0:
                return ans
            if i in inv_store:
                current = inv_store[i]
                if len(current) >= left:
                    ans.extend(current[0:left])
                    return ans
                else:
                    ans.extend(current)
        return ans