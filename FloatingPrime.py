'''
    Question: [2] Floating Prime
    Author: Passawit Riewthong
'''


def isPrime(num):
    # Function to check the number is a prime number

    if num > 1:
        for i in range(2, num):
            # Check for a product of two smaller numbers
            if (num % i) == 0:
                return False  # Is not prime number
        else:
            return True  # Is prime number
    else:
        return False  # Less than 1 is not prime number


while True:
    # Get input and formatting
    num = input().replace('.', '')
    if num == '00':
        break  # End program

    # Check for 1st decimal place
    if isPrime(int(num[0:2])):
        print('TRUE')
        continue

    # Check for 2nd decimal place
    if isPrime(int(num[0:3])):
        print('TRUE')
        continue

    # Check for 3rd decimal place
    if isPrime(int(num[0:4])):
        print('TRUE')
        continue

    print('FALSE')  # Not Floating Prime
