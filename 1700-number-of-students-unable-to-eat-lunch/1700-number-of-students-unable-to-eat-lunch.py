class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        counter = 0 
        
        while len(students) > 0 and counter < len(students):
            if sandwiches[0] == students[0]:
                students.popleft()
                sandwiches.popleft()
                counter = 0
            else:
                temp = students.popleft()
                students.append(temp)
                counter += 1
        
        return counter 
            
        