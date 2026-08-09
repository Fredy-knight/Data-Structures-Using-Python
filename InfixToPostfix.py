operators =  ['+','-','*','/','(',')']
lvl = {'+':1,'-':1,'*':2,'/':2,'^':3}
def infix_to_postfix(expression):
    stack=[]
    output=''
    for i in expression:
        if i not in operators:
            output+=i
        elif i =='(':
            stack.append(i)
        elif i ==')':
            while stack and stack [-1]!= '(':
                output+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!= '(' and priority [i]<=priority[stack[-1]]:
                output+=stack.pop()
            stack.append(i)
    while stack:
        output+=stack.pop()
    return output
expression = input("Enter the infix expression:")
print("The appropriate postfix expression is :",infix_to_postfix(expression))

                
    
    
