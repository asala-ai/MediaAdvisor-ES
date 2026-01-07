# main.py
from advisor import advise

print("Welcome to Media Advisor Expert System")

target = input("Enter target audience (youth/adults/business): ").lower()
budget = input("Enter budget (low/medium/high): ").lower()

result = advise(target, budget)
print("Recommended Media Strategy:", result)