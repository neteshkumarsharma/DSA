class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:#
        stack = []
        num = 1
        j = 0
        while j < len(target):
            stack.append('Push')
            if num != target[j]:
                stack.append('Pop')
                num += 1
            else:
                j += 1
                num += 1
        return stack