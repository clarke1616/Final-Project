###form 1040, 2022 Tax Year

'''
print('Welcome! The personal account is ready to do your taxes!')




print ("By running this program, you will be asked a series a questions that will be used to calculate the line items on your form 1040.")
print ("In order to complete this document, you will need to have the following forms:")
print ('            - W-2')
print ('            - 1099- IOD (if applicable)')
print ('            - 1099- DIV')
print ('            - 1099- R')
print ('            - SSA- 1099')
print ('            - Schedual 1')
print ('            - Schedual D (if applicable)')
print ('')
print('')
'''
#############################################################################################################################################

##Inputs needed

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
     
##For lines 3a and 3 b
qd = int(input ("Looking at line 1b on your 1099-DIV, please enter the number given"))
od = int(input ("Looking at line 1a on your 1099-DIV, please enter the number given"))

##For lines 4a and 4b
r = input('Looking at your form 1099-R, is there any IRA Distrubutions being rolledover from previous years? (Y or N)')
if r == 'y' or r == 'Y':
     amount = int(input('How much is being rolled over?'))
else:
     amount = 0

IRATax = int(input('Looking at your 1099-R, what is the amount in box 1?'))


##Lines 5a and 5b
taxableAnnuities = int(input('Looking at your form 1099-R, what amount of your Pensions and Annuities are tax exempt?'))


#Lines 6a & 6b
socsecTotal = int(input('Looking at your SSA-1099, what is the amount in box 3?'))
socsecPaid = int(input('Looking at your SSA-1099, what is the amount in box 4?'))               

##Line 7

capital = input('Did you sell any capital assets? (Y or N)')
if capital == 'y' or capital == 'Y':
     capamount = int(input('What is your capital gain or loss?'))
else:
     capamount = 0

##line 8

other = int(input('Looking at Schedule 1, what is the amount on line 10?'))

#line 10
adj = int(input('Looking at Schedule 1, what is line 26?'))

#Line 12a
deduction = input('are you filing as: A - Single B - Married Filing seperatly C- Married filing jointly D- Qualified Widow, or E - Head of household?')

##Line 12b
don = int(input('How much did you donate to charity this year? **MAX $300 for single and $600 joint**'))

################################################################################################################################################

#Calculations

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

##Line 3a - Qualified Dividends
def qualifiedDividends():
     Qdiv = qd
     return qd

##Line 3b - Ordinary Dividends
def ordinaryDiv():
     OrdDiv = od
     return OrdDiv
##Line 4a - IRA Distributions
def IRADistributions():
     twoa = amount
     return twoa
##Line 4b
def IRADistTaxableAmount():
     IRAT = IRATax
     return IRAT

##Line 5a
def pensionsAndAnnunities():
     pataxable = taxableAnnuities
     return  pataxable
##Line 5b
def taxablePensionsAndAnnuities():
     totalAandP = IRATax
     taxedPanda = totalAandP - pensionsAndAnnunities()
     return taxedPanda
##Line 6a
def socialsecuritybenefits():
     totalsocialsecurity = socsecTotal
     return totalsocialsecurity
##Line 6b
def taxedsocialsecurity():
     taxedss = socsecPaid
     return taxedss
##Line 7
def capitalgl():
     capgainloss = capamount
     return capgainloss
##line 8
def otherincome():
     otherinc = other
     return otherinc
##line 9

def totalincome():
     tot = wagesAndSalaries() + taxableInterest() + ordinaryDiv()+ IRADistTaxableAmount()+ taxablePensionsAndAnnuities()+ taxedsocialsecurity()+ capitalgl()+ otherincome()
     return tot


##Line 10
def adjToIncome():
     adjustments = adj
     return adjustments

#Line 11
def AGI ():
     agi = totalincome() - adjToIncome()
     return agi
     
##Line 12a
def deductions():
     deductionAmount = 0
     deduct = deduction
     if deduct == 'A' or deduct == 'a' or deduct == 'B' or deduct == 'b':
          deductionAmount += 12550
     elif deduct == 'C' or deduct == 'c' or deduct == 'D' or deduct == 'd':
          deductionAmount += 25100
     elif deduct == 'E' or deduct == 'e':
          deductionAmount += 18800
     return deductionAmount

##Line 12b
def twelveb():
     d = don
     return d
##Line 12c
def twelveC():
     twelveTotal = twelveb()+ deductions()
     return twelveTotal


################################################################################################################################################################
print('')
print('')
print('')
print('')
print('')
print('')

print('Your 1040 Tax form should be filled out as follows:')
print('')
print('')
print('')

print ('')
print ('1. Wages, salaries, tips etc. Attach From(s)  W-1 . . . . . . . . . . . . . . . . ' ,wagesAndSalaries())
print ('2a. Tax-exempt interest . . . 2a  ', exemptInterest(), '      b  Taxable Interest  . . . . . . . . 2b', taxableInterest())
print ('3a. Qualified dividends . . . 3a  ', qualifiedDividends(), '      b  Ordinary dividends. . . . . . . . 3b',ordinaryDiv())
print ('4a. IRA Distributions. . . . .4a  ', IRADistributions(),'      b  Taxable amount  . . . . . . . . . 4b', IRADistTaxableAmount())
print ('5a. Pensions and annuities . .5a  ', pensionsAndAnnunities(),'      b  Taxable amount  . . . . . . . . . 5b', taxablePensionsAndAnnuities())
print ('6a. Social security benefits .6a  ', socialsecuritybenefits(), '      b  Taxable amount . . . . . . . . . .6b', taxedsocialsecurity())
print ('7 Capital gain or (loss). Attach Schedule D is required. If not, check here . . 7 ', capitalgl())
print ('8 Other income from Schedule 1, line 10 . . . . . . . . . . . . . . . . . . . . 8 ',otherincome())                           
print ('9 Add lines 1, 2b, 3b, 4b, 5b, 6b, 7 and 8. This is your total income . . . . . 9 ', totalincome())                            
print ('10 Adjustments to income from Schedule 1, line 26 . . . . . . . . . . . . . . .10 ', adjToIncome())
print ('11 Subtract line 10 from line 9. This is your adjusted gross income . . . . . .11 ', AGI())
print ('12a Standard Deduction or itemized deductions (from schedule A) . . 12a', deductions())
print ('  b Charitable contributions id you take the standard deduction . . 12b',twelveb())     
print ('  c Add lines 12a and 12b . . . . . . . . . . . . . . . . . . . . . . . . . . .12c',twelveC())                     
                      
                     
    
