class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        key_comb = {"2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        combination = [""]
        
        for d in digits:
            temp = []
            for i in combination:
                for ch in key_comb[d]:
                    temp.append(i+ch)
            combination = temp
        return combination

        