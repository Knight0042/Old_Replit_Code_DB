student_total1 = float(input('Student Total 1: '))
student_total2 = float(input('Student Total 2: '))
Max1 = float(input('Max Total 1: '))
Max2 = float(input('Max Total 2: '))
if Max1 == 0:
    Max1 = 1
if Max2 == 0:
    Max2 = 1
weight1 = float(input('Weight of First Total: '))
weight2 = float(input('Weight of Second Total: '))
total1 = (student_total1/Max1)*weight1
total2 = (student_total2/Max2)*weight2
end_percentage = (total1+total2)

print('The End Percentage is: %', end_percentage)
