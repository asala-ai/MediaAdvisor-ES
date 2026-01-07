# advisor.py
# Inference Engine for Media Advisor Expert System

from rules import rules

def advise(target, budget):
    for rule in rules:
        if rule["target"] == target and rule["budget"] == budget:
            return rule["media"]
    return "No suitable media strategy found"
