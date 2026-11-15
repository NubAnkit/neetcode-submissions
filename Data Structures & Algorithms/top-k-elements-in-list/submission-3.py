class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        inv_store = defaultdict(list)
        ans = []
        for i in nums:
            if i in store:
                store[i] += 1
            else:
                store[i] = 1
        for u, v in store.items():
            inv_store[v].append(u)
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