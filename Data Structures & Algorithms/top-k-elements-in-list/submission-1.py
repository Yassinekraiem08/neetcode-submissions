import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for number in nums:
            if number in counter:
                counter[number] += 1
            else:
                counter[number] = 1
                
        heap = []
        for number, frequency in counter.items():
            heapq.heappush(heap, (frequency, number))
            if len(heap) > k:
                heapq.heappop(heap)


        result = []
        for frequency, number in heap:
            result.append(number)
            
        return result
