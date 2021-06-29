
# A program for Fibonacci numbers.

terms = int(input('Number of Terms: '))

n1 = 0
n2 = 1
sum = 0

if terms < 0:
    print('Please, Enter a positive integer.')
elif terms == 1:
    print(f'Fiboncci Sequence upto {terms} term is:\n', n1)
else:
    print(f'Fibonacci Sequence upto {terms} terms is:')
    while sum < terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        sum += 1

