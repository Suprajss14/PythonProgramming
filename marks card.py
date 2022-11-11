#marks card
print('Enter 3 internal marks')
marks1=int(input('Marks scored in first IA'))
marks2=int(input('Marks scored in second IA'))
marks3=int(input('Marks scored in third IA'))
if marks1<marks2 and marks1<marks3:
    print('average of best two marks',(marks2 + marks3)/2)
elif marks2<marks1 and marks2<marks3:
    print('average of best two marks',(marks1 + marks3)/2)
elif marks3<marks1 and marks3<marks2:
    print('average of best two marks',(marks1 + marks2)/2)