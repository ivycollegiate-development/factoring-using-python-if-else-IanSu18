a = int(input('If a is the factor of b? a= '))
b = int(input('If a is the factor of b? b= '))
def is_factor(a, b): 
    if b % a == 0:
        return True 
    elif a % b != 0:
        return False
def answer():
    if is_factor(a, b) == True:
        print(f'Yes, {a} is a factor of {b}.')
    elif is_factor(a, b) == False:
        print(f'No, {a} is not a factor of {b}.')
    else:
        return none 
print(answer())