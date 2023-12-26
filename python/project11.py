def isPalindrome(str):
    starindex =0
    endindex = len(str)-1

    for x in str:
        if str[starindex] != str[endindex]:
           print('this is not palidrome')
    else:
       print('This is  palidrome')
    

print(isPalindrome (input('Enter your value to check Palidrome: ')))
