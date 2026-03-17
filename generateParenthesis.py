"""
Problem:
Given n pairs of parentheses, generate all combinations of well-formed parentheses.

Example:

Input: n = 3
Output:
[
 "((()))",
 "(()())",
 "(())()",
 "()(())",
 "()()()"
]

Let:
open = number of '(' used
close = number of ')' used
Rules:
You can add '(' if:
  open < n

You can add ')' if:
  close < open
(otherwise invalid)

👉 This is the core idea of the problem
"""

def generateParenthesis(n):
    result = []

    def backtrack(curr, open_count, close_count):
        # Step 1: base case
        if len(curr) == 2 * n:
            result.append(curr)
            return

        # Step 2: add '(' if possible
        if open_count < n:
            backtrack(curr + "(", open_count + 1, close_count)

        # Step 3: add ')' if valid
        if close_count < open_count:
            backtrack(curr + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result
