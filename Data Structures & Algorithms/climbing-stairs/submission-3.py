class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        sequence = [1, 2]
        for i in range(2, n):
            sequence.append(sequence[i-1] + sequence[i-2])
        
        return sequence[-1]