class Solution:
    def calPoints(self, operations: List[str]) -> int:
        int_lst = []
        for i in range (len(operations)):
            if operations[i] == "+":
                int_lst.append(int_lst[-1]+int_lst[-2])
            elif operations[i] == "D":
                int_lst.append(int(int_lst[-1])*2)
            elif operations[i] == "C":
                int_lst.pop()
            else:
                int_lst.append(int(operations[i]))
        print(int_lst)
        return sum(int_lst)

            
        