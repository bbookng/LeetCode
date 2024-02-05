class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        duplicated = dict()

        answer = 0

        for right, alpha in enumerate(s):
            if alpha in duplicated and duplicated[alpha] >= left:
                print(duplicated[alpha], alpha, left)
                left = duplicated[alpha] + 1
            else:
                answer = max(answer, right - left + 1)
            duplicated[alpha] = right

        return answer

