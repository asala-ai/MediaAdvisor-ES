## Conflict Resolution in Media Advisor Expert System

### Conflicting Scenario
A conflict occurs when multiple rules match the same input.
For example, a youth audience with a low budget can match more than one media strategy.

### Conflict Resolution Method
The system applies a **Priority-Based Conflict Resolution** approach.
Each rule is assigned a priority, and the rule with the highest priority is selected.

### Why Priority Method?
- Simple and effective
- Common in rule-based expert systems
- Ensures consistent decisions
- Suitable for small and medium expert systems

### Example
Two rules apply:
- Youth + Low Budget → Social Media Ads
- Youth + Low Budget → Email Campaign

The system selects the rule with higher priority.

### Implementation
The conflict resolution mechanism is implemented in Python inside the inference engine.
