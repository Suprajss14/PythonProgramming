#designing a chatbot using if else
print('hello, iam a chatboot')
print('how may i heplp you?\n')
print('hit 1 for software installation request')
print('hit 2 for software update request')
print('hit 3 for software uninstall request')
print('hit 4 for software repair request')
print('hit 5 for other request')
#accepting the user input
userinput = int(input('Enter your choice'))
#using if else to process the input
if userinput == 1:
    softwareneeded = input('please provide the software name')
elif userinput == 2:
    softwareupdate = input('Please provide the software name to be updated')
elif userinput == 3:
    softwareuninstall = input('Please provide the software name to be uninstalled')
elif userinput == 4:
    softwarerepair = input('Please provide the software name to be repaired')
else: #else is the end and we cannot ada another elif
    otherrequest = input('Please provide the details of your request')
print('Thank you for using our service, our team will get back you soon')

