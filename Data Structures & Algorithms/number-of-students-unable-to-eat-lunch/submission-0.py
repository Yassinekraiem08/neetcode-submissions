class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = collections.deque(students)
        sandwiches = collections.deque(sandwiches)
        rotations = 0
        while students and rotations < len(students):
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                rotations = 0
            else:
                students.append(students.popleft())
                rotations += 1
        

        return len(students)