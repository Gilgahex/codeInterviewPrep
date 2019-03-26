def valid_parentheses(string):
    paren = ""
    for i in string:
        if i == '(' or i == ')':
            paren+=i
    print(paren)
    stack = []
    for ch in paren:
        if ch == '(':
            stack.append(')')
        elif not stack or stack.pop() != ch:
            return False
    return stack == []
 
s = "hi(hi)()"
print(valid_parentheses(s))
