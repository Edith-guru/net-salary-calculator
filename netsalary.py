# basic_salary = float(input("enter your basic salary"))
# benefits = float(input("enter your benefits"))
#from salary import nssf


gross_salary = float(input("Please enter your Gross salary:"))

nssf = 200
personal_relief = 2400
def taxable_income():
    ti = gross_salary - nssf
    return ti
taxable_income()

def nhif_deductable():
    if gross_salary > 0 and gross_salary <= 5999:
        nd  = 150
    elif gross_salary >= 6000  and gross_salary <= 7999:
        nd  = 300
    elif gross_salary >= 8000  and gross_salary <= 11999:
        nd  = 400
    elif gross_salary >= 12000 and gross_salary <= 14999:
        nd  = 500
    elif gross_salary >= 15000 and gross_salary <= 19999:
        nd  = 600
    elif gross_salary >= 20000 and gross_salary <= 24999:
        nd  = 750
    elif gross_salary >= 25000 and gross_salary <= 29999:
        nd  = 850
    elif gross_salary >= 30000 and gross_salary <= 34999:
        nd  = 900
    elif gross_salary >= 35000 and gross_salary <= 39999:
        nd  = 950
    elif gross_salary >= 40000 and gross_salary <= 44999:
        nd  = 1000
    elif gross_salary >= 45000 and gross_salary <= 49999:
        nd  = 1100
    elif gross_salary >= 50000 and gross_salary <= 59999:
        nd  = 1200
    elif gross_salary >= 60000 and gross_salary <= 69999:
        nd  = 1300
    elif gross_salary >= 70000 and gross_salary <= 79999:
        nd  = 1400
    elif gross_salary >= 80000 and gross_salary <= 89999:
        nd  = 1500
    elif gross_salary >= 90000 and gross_salary <= 99999:
        nd  = 1600
    elif gross_salary >= 100000:
        nd  = 1700
    return nd
print(nhif_deductable())

def payee():
    tax = 0
    if taxable_income() <= 24000:
        tax = tax + (taxable_income() * 0.1)
    elif taxable_income() <= 32333:
        tax = ((taxable_income() - 24000) * 0.25)+ 2400
    else:
        tax = ((taxable_income() - 32333) * 0.3) + 4483
    return tax - personal_relief
payee()

def deductables():
    dd = payee() + nhif_deductable() + nssf
    return dd
deductables()

def net_salary():
    ns = (gross_salary - deductables())
    return ns
print(net_salary())

