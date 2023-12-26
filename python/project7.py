leap = False
is_leap=True
    
    # Write your logic here
year = int(input('Enter your year: '))
    
if year % 4 == 0:
    print(is_leap)
elif year % 100==0:
    if year % 400==0:
        print(is_leap)
elif year % 100==0:
    if year % 400 !=0:
        print(leap)
else:
    print(leap)