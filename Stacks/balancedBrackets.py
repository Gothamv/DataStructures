"""
A program to check if the brackets are balanced.
A balanced set of brackets is one where the number and type of opening and closing brackets match that is also properly nested within the string of brackets.
"""
from stacks import Stack

def isAMatch(s1: str, s2: str) -> bool:
  if s1 =='(' and s2 == ')':
    return True
  elif s1 == '[' and s2 == ']':
    return True
  elif s1 == '{' and s2 == '}':
    return True
  else:
    return False

def isBracketBalanced(string: str) -> bool:
  
  bracketStack = Stack()
  isBalanced = True
  index = 0

  while index < len(string) and isBalanced:
    x = string[index]
    if x in "({[":
      bracketStack.push(x)
    else:
      if bracketStack.isEmpty():
        isBalanced = False
      else:
        top = bracketStack.pop()
        if not isAMatch(top, x):
          isBalanced = False
    index += 1

  if bracketStack.isEmpty() and isBalanced:
    return True
  else:
    return False

print("{([])} isBalanced? : ", isBracketBalanced("{([])}"))
print("{([]} isBalanced? : ", isBracketBalanced("{([]}"))
print("[][] isBalanced? : ", isBracketBalanced("[][]"))
print("[]{} isBalanced? : ", isBracketBalanced("[]{}"))
