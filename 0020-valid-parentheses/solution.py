from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in ")}]":
                if not stack:
                    return False
                if c == ")" and stack[0] != "(":
                    return False
                if c == "}" and stack[0] != "{":
                    return False
                if c == "]" and stack[0] != "[":
                    return False
                stack.popleft()
            else:
                stack.appendleft(c)
        return len(stack) == 0
