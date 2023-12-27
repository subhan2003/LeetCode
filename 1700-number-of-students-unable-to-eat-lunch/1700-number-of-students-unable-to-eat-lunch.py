class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = 0 
        while len(students) > 0 and counter < len(students):
        
            if sandwiches[0] == students[0]:
                students.pop(0)
                sandwiches.pop(0)
                counter = 0
                
            else:
                temp = students.pop(0)
                students.append(temp)
                counter += 1
        
        return counter 
            
        