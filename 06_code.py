""" Calculate the compound interest for a given principal
amount, interest rate, and time period"""

"""A = P * (1 + r/100) ** t
A = Final amount
P = Principal (initial money)
r = Interest rate (%)
t = Time (years)"""

def compound_interest(p, r, t):
    amount = p * (1 + r / 100) ** t
    ci = amount - p
    return ci

principal = 1000
rate = 5
time = 2

ci = compound_interest(principal, rate, time)
print("Compound Interest:", ci)