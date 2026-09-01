class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        output = len(students)
        count = Counter (students)

        for s in sandwiches:
            if count[s] > 0:
                count[s] -= 1
                output -= 1
            else:
                break

        return output