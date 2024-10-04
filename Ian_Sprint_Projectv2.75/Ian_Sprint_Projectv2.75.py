a = int(input('If a is the factor of b? a= '))
b = int(input('If a is the factor of b? b= '))
def is_factor(a, b): 
    if b % a == 0:
        return True 
    elif a % b != 0:
        return False
if is_factor == True:
    print(f'Yes, {a} is a factor of {b}.')
elif is_factor == False:
    print(f'No, {a} is not a factor of {b}.')
print(is_factor(a, b))