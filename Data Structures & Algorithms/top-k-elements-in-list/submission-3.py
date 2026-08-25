import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        heap = []
        for number, frequency in count.items():
            heapq.heappush(heap, (frequency, number))
            if len(heap) > k:
                heapq.heappop(heap)
        
        output = []
        for frequency, number in heap:
            output.append(number)
        
        return output