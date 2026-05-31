class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        out = []
        temp = []
        for i in range(1,n+1):
            out.append("Push")
            temp.append(i)
            if i not in target:
                out.append("Pop")
                temp.pop()
            if temp == target:
                break
        return out


