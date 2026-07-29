class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        h = [(-freq, word) for word, freq in counter.items()]

        heapq.heapify(h)
        return [heapq.heappop(h)[1] for _ in range(k)] 