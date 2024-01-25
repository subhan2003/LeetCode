class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for i in range(len(operations)):
            x = operations[i]

            if x == 'C':
                record.pop()
            elif x == 'D':
                y = record[-1] * 2
                record.append(y)
            elif x == '+':
                z = record[-1] + record[-2]
                record.append(z)
            else:
                record.append(int(x))
                
        total = sum(record)
        return total