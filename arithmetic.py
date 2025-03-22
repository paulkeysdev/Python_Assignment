#asks users for thier details
val_1 =float(input(f'Enter the first number:'))
val_2=float(input(f'Enter the other number:'))
val_3=(input(f'Enter a mathematical Operation(*, +, -, /):'))
if val_3=='*': 
    result = val_1 * val_2
elif val_3 == '+':
    result = val_1 + val_2
elif val_3 == '-':
    result = val_1 - val_2
elif val_3 == '/':
    result = val_1 / val_2
else:
    print(f'Invalid Operation')
print(f'The result of your operation is {result}')      