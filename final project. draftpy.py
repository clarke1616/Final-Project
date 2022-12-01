###form 1040, 2022 Tax Year

#print ("By running this program, you will be asked a series a questions that will be used to calculate the line items on your form 1040.")
#print ("You will need access to your W-2 form as well as your 1099 -IOD form if you have recieved interest this tax year")

##Line 1 - Wages Salaries and Tips Etc
a = int(input ("What was your total wages, salaries and tips for 2022 - this can be found in BOX 1 of your W-2."))
##For line 2a
b = input("Did you recieve any interest in 2022 from municiple (state) bonds? Y or N")
if b == 'Y' or b == 'y':
        box2 = int(input ("What is box 2 on your 1099-OID?"))
        box11 = int(input ("What is box 11 on your 1099-OID?"))
else:
     box2 =0
     box11 = 0
##For line 2b
c = input("Did you recieve any interest in 2022 excluing interest from municiple (state) bonds? Y or N")
if c == 'Y' or c == 'y':
     x = int(input('What is the total taxable interest income found on your 1099-IOD?' ))
        #return line2b
else:
     x = 0

def wagesAndSalaries():
     #line1 = int(input ("What was your total wages, salaries and tips for 2022 - this can be found in BOX 1 of your W-2."))
     line1 = a
     return line1


## Line 2a - Tax exempt Interest

def exemptInterest ():
    #ei = input("Did you recieve any interest in 2022 from municiple (state) bonds? Y or N")
    #ei = b  
    #if ei == 'Y' or ei == 'y':
        #oidBox2 = int(input ("What is box 2 on your 1099-OID?"))
        #oidBox11 = int(input ("What is box 11 on your 1099-OID?"))
    b2 = box2
    b11 = box11
    line2a =  box2 + box11
    return line2a
    #else:
        #line2a = 0
        #return line2a
##figure out how to get them all to print at the bottom

#print ('Line 2a = ', exemptInterest())

##Line 2b - taxable interest
def taxableInterest ():
    ti = x
    #ti = input("Did you recieve any interest in 2022 excluing interest from municiple (state) bonds? Y or N")
    #if ti == 'Y' or ti == 'y':
        #line2b = int(input('What is the total taxable interest income found on your 1099-IOD?' ))
       # return line2b
    #else:
        #line2b = 0
    return ti
#print ('Line 2b =',taxableInterest())



print('Your 1040 Tax form should be filled out as follows:')
print ('1. Wages, salaries, tips etc. Attach From(s) W-1 . . . . . . . . . . . . . . . . ' ,wagesAndSalaries())
print ('2a. Tax-exempt interest . . . 2a', exemptInterest(), '              b    Taxable Interest . . . . .', taxableInterest())
