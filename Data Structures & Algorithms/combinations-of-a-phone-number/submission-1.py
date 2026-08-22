class Solution:

    digitsToLetter = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return [char for char in self.digitsToLetter[digits[0]]]
        else:
            subOutputs = self.letterCombinations(digits[1:])
            ans =[]
            for char in self.digitsToLetter[digits[0]]:
                for subOutput in subOutputs:
                    ans.append(char + subOutput)
            return ans

