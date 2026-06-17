class Solution:
    def processStr(self, s: str) -> str:
        result = ""
        n = len(result)
        for i in s:
            if i.isalpha():
                result += i
            else:
                if i == "*" and result != "":
                    result = result[0:n-1]
                elif i == "%" and result != "":
                    result = result[::-1]
                elif i == "#" and result != "":
                    result = result*2
                else:
                    pass
        return result