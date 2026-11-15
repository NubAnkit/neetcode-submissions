class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = defaultdict(list)
        ans = []
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for u, v in count.items():
            buckets[v].append(u)
        for i in range(len(nums), 0, -1):
            left = k - len(ans)
            if left == 0:
                return ans
            if i in buckets:
                current = buckets[i]
                if len(current) >= left:
                    ans.extend(current[0:left])
                    return ans
                else:
                    ans.extend(current)
        return ans