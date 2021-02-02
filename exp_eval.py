from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    '''Evaluates a postfix expression
    
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''

    stack_lst = input_str.split(" ")
    
    operator = 0
    operand = 0
    invalid = 0
    for n in stack_lst:
        if n == "+" or n == "-" or n == "*" or n == "/" or n == "**":
            operator += 1
        elif is_num(n):
            operand += 1
        else:
            invalid += 1
    if operand == 0 and operator == 0 or invalid >= 1:
        raise PostfixFormatException("Invalid token")
    if operand - operator < 1:
        raise PostfixFormatException("Insufficient operands")
    elif operand - operator > 1:
        raise PostfixFormatException("Too many operands")

    stack = Stack(len(stack_lst))

    for token in stack_lst:
        if token == "+":
            num_2 = stack.pop()
            num_1 = stack.pop()
            stack.push(num_1 + num_2)
        elif token == "-":
            num_2 = stack.pop()
            num_1 = stack.pop()
            stack.push(num_1 - num_2)
        elif token == "*":
            num_2 = stack.pop()
            num_1 = stack.pop()
            stack.push(num_1 * num_2)
        elif token == "/":
            num_2 = stack.pop()
            num_1 = stack.pop()
            if num_2 == 0:
                raise ValueError
            stack.push(num_1 / num_2)
        elif token == "**":
            num_2 = stack.pop()
            num_1 = stack.pop()
            stack.push(num_1 ** num_2)
        else:
            stack.push(float(token))
    
    final = stack.pop()
    return final

    
def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)'''
    stack_lst = input_str.split(" ")
    stack_lst.reverse()
    stack = Stack(len(stack_lst))

    for token in stack_lst:
        if is_num(token):
            stack.push(token)
        else:
            stack.push(stack.pop() + " " + stack.pop() + " " + token)
    final_string = stack.pop()
    return final_string


#str -> boolean
#Returns true if string is a number
def is_num(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
