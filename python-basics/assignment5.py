#Name : Bob Afwata
# Date : 11/02/2026
# Program to  calculate income tax

salary = int(input("Enter your gross salary :"))

if salary < 50000:
    tax = (2.5 * salary) / 100 
    net_salary = salary - tax 

print(f"Gross salasy = {salary}")
print(f"Net salasy = {net_salary}")
print(f"Tax = {tax}")