import re
class Solution:
    def simplifyPath(self, path: str) -> str:
        # cleaned_path = re.sub(r'/+', '/', path)
        op = []
        for i in path.split("/"):
            print(i)
            if i == "" or i == ".": #그냥일때
                continue
            elif i == "..": #뒤로갈때
                if op:
                    op.pop()
            else:
                op.append(i)
        return "/"+"/".join(op)


                        



