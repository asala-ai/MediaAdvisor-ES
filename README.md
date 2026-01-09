# Media Advisor Expert System

This project is a **Media Advisor Expert System** implemented in Python.  
It recommends a suitable media strategy based on the target audience and budget level.

## Project Description
- The system determines the optimal media strategy based on:
  - Target Audience (Youth, Adults, Business)
  - Budget Level (Low, Medium, High)
- Technologies used:
  - Python 3
  - Rule-Based Expert System (Inference Engine)

## Conflict Resolution in Media Advisor Expert System
- **Conflicting Scenario:**  
  A conflict occurs when multiple rules match the same input.  
  Example: Youth audience with a Low budget can match more than one media strategy.

- **Conflict Resolution Method:**  
  A **Priority-Based Conflict Resolution** approach is applied. Each rule is assigned a priority, and the rule with the highest priority is selected.

- **Why Priority Method?**
  - Simple and effective
  - Common in rule-based expert systems
  - Ensures consistent decisions
  - Suitable for small and medium expert systems

- **Example:**  
  Two rules apply:  
  1. Youth + Low Budget → Social Media Ads  
  2. Youth + Low Budget → Email Campaign  
  The system selects the rule with the higher priority.

- **Implementation:**  
  The conflict resolution mechanism is implemented in Python inside the inference engine.
