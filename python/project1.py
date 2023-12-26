bill_total = int(input('enter your bill amount: '))


discunt1=300

if bill_total >1000 and bill_total <=1500:
    print("total bill is greater than 1000!")
    bill_total=bill_total-discunt1
elif bill_total > 1500:
    print("bill is greater than 1500")
else:
    print ("bill is less than 1000")

print('your total bill: ' + str(bill_total))