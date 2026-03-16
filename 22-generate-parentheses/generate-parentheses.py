class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backTracking(openLeft, closeLeft, currentStr, result):
            if openLeft == 0 and closeLeft == 0:
                result.append(currentStr)
                return
            
            if openLeft > 0:
                backTracking(openLeft - 1, closeLeft, currentStr + '(', result)
            if closeLeft > openLeft:
                backTracking(openLeft, closeLeft - 1, currentStr + ')', result)
        result = []
        backTracking(n, n, '', result)
        return result