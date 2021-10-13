# variables

meal = float(input('enter cost food $: '))
people = float(input('enter # people splitting total: '))
tip = float(input('enter tip %: '))
tax = .10

# math

tip_amt = meal * tip/100

tax_amt = meal * tax

total = meal + tip_amt + tax_amt

each = total / people

# print output

print (f'\nmeal is ${meal:.2f} and tip is ${tip_amt:.2f}.')

print (f'total with 10% tax is ${total:.2f}.\n')

print (f'each person pays ${each:.2f}.\n')

# final comment on how programmer feels

print ('This works great!')