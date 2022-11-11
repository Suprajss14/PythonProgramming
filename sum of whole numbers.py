#finding the sum of first n whole numbers using the loop
endpoint = int(input('entering the value of n:'))
sum_of_numbers = 0
for i in range(endpoint):
    print('sum of numbers value is:', sum_of_numbers)
    print('index i value is:',i)
    sum_of_numbers = sum_of_numbers + i
print('the sum of first {} whole numbers is {}'.format(endpoint,sum_of_numbers))