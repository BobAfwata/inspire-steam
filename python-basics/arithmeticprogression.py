#Name : Bob Afwata
# Date : 13/02/2026
# Program to calculate aithmetic progression

# Calculating nth term

a = int(input("Enter the first number :"))
n = int(input("Enter the number of terms :"))
d = int(input("Enter the common difference :"))

nth_term = a + (n - 1) * d
sn = (n/2) *( (2*a) +(n-1) *d )
print(f"The nth Term is  :  {nth_term}") 