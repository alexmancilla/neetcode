class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for element in operations:
            if element == "+":
                record.append(record[-1] + record[-2])
            elif element == "D":
                record.append(record[-1] * 2)
            elif element == "C":
                record.pop()
            else:
                record.append(int(element))  # aquí entra "2", "-2", "10", etc.

        return sum(record)

        # 3, 9, 5, 10,     



        