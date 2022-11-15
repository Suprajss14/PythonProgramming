num = int(input('How many numbers: '))
total_sum = 0
for n in range(num):
    numbers = float(input('Enter number : '))
    total_sum += numbers
avg = total_sum/num
print('Average of ', num, ' numbers is :', avg)
if (avg>=5):
    print("your numbers are small")
elif (avg<=100)and(avg>5):
    print("your numbers are large")