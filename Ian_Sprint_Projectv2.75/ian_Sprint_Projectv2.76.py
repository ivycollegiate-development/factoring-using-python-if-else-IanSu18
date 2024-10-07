def list_factor(n):
    return [i for i in range (1, n+1) if n % i == 0 ]
    #This line of code list out every number that n are divisible by the number i. Which i is every number from 1 to n. 

if __name__ == '__main__':
    user_input = input('Please enter a number here: ')
try:
    number = int(user_input)
    if number <= 0:
        print('please enter a positive number.')
    else:
        factors = list_factors(number)
        print(f'The factor of {number} are {factors}')
except ValueError:
    print('THat is an invalid number, Please input a positive interger')