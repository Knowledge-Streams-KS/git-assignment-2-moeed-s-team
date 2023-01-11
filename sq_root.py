import math # import the math module

def sq_root(num1, num2):
    num1_sqrt = math.sqrt(num1) 
    num2_sqrt = math.sqrt(num2) #taking square root of both numbers and storing it in different variables

    sq1 = f'{num1_sqrt:.3f}'
    sq2 = f'{num2_sqrt:.3f}'
    
    print(f"Square root of {num1} = {sq1}")
    print(f"Square root of {num2} = {sq2}")