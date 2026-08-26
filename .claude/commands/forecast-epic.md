---
description: "Epic completion forecast based on historical epic velocity and story count analysis"
---

# Epic Completion Forecast Command

You are executing the `/forecast-epic` command to forecast how many sprints a target epic will take to complete based on historical epic completion data.

## Configuration

**Settings:**
- **Target project:** where the epic lives (default: `[PRODUCT_PROJECT]`).
- **Reference project:** whose completed stories define velocity. **Defaults to the same project as the epic.** Only point this at a separate delivery/engineering project if you track execution separately, and note the reference stories should be comparable in size to the epic's stories, or the forecast skews.
- **Optimistic Multiplier:** 1.2x (increased velocity assumption)
- **Conservative Multiplier:** 0.8x (reduced velocity assumption)
- **Output:** Always generate PNG visualization chart

## Workflow

### 1. Gather Information

Use AskUserQuestion to collect:

**Question 1: Target Epic & Projects**
- Which epic do you want to forecast? (e.g., "[PRODUCT_PROJECT]-34")
- Which project should I measure velocity from? (default: the same project as the epic; name a separate delivery/engineering project only if you track execution there)

**Question 2: Story Prefixes for Reference Velocity**
- Which story prefixes should I consider for calculating historical velocity?
- Examples: "[Module A] -", "[Module B] -" (use your own module/feature-area prefixes)
- Can select multiple prefixes

**Question 3: Sprint Range for Reference**
- Which sprints should I use for reference velocity? (e.g., "Sprints 1-6")

**Question 4: Target Epic Story Filter**
- Should I consider ALL stories in the target epic, or only stories with specific prefixes?
- If prefixes: which ones? (e.g., "[Module] -")

**Question 5: Current Sprint**
- What is the current sprint number? (e.g., "Sprint 7")

**Question 6: Completion Assumption**
- Should I assume all stories are incomplete (0 done), or use actual Jira status?

### 2. Fetch Reference Velocity Data (reference project)

Query Jira for completed stories in the **reference project** (from Question 1, defaults to the epic's own project) with the specified prefixes:

```jql
project = [PRODUCT_PROJECT] AND issuetype = Story AND status = Done AND (summary ~ "Prefix1 -" OR summary ~ "Prefix2 -") ORDER BY created DESC
```

(If you named a separate delivery project in Question 1, use that project key instead.)

**Filter by sprint range** using the `customfield_10020` (sprint field) data.

**Calculate:**
- Total stories completed with specified prefixes
- Number of sprints in range
- **Epic velocity:** stories completed ÷ sprints

### 3. Fetch Target Epic Data ([PRODUCT_PROJECT] Project)

Query Jira for the target epic stories:

```jql
project = [PRODUCT_PROJECT] AND issuetype = Story AND "Parent Link" = <EPIC-KEY> ORDER BY created DESC
```

**If filtering by prefix:**
```jql
project = [PRODUCT_PROJECT] AND issuetype = Story AND "Parent Link" = <EPIC-KEY> AND summary ~ "Prefix -" ORDER BY created DESC
```

**Collect:**
- Total stories matching filter
- Completed stories (if using actual status)
- Remaining stories

### 4. Run Forecast Scenarios

Calculate 4 scenarios using the reference velocity:

#### 1️⃣ Linear Projection
- Formula: Reference sprints × (Target stories / Reference stories)
- Assumes linear scaling based on story count ratio

#### 2️⃣ Velocity-Based
- Formula: Remaining stories / Reference velocity
- Uses actual historical velocity from the reference project

#### 3️⃣ Conservative (0.8x)
- Formula: Remaining stories / (Reference velocity × 0.8)
- Accounts for increased complexity, reduced capacity

#### 4️⃣ Optimistic (1.2x)
- Formula: Remaining stories / (Reference velocity × 1.2)
- Accounts for team learning, improved efficiency
- **Note:** Uses the standard 1.2x optimistic multiplier

### 5. Generate Visualization Chart

**ALWAYS create a PNG chart** saved to:
```
forecasts/<epic-name>-forecast.png
```

**Chart must include:**

**Left Panel - Epic Story Comparison:**
- Bar chart comparing reference stories vs target stories
- Color-coded: green for completed, red for remaining
- Show story counts on bars

**Right Panel - Sprint Forecast Scenarios:**
- Horizontal bar chart with all 4 scenarios:
  - Optimistic (1.2x) - green
  - Linear Projection - blue
  - Velocity Based - purple
  - Conservative (0.8x) - orange
- Sprint estimates labeled on each bar
- Average line (dashed red)
- Target sprint numbers on secondary x-axis

**Use this Python template:**

```python
import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Epic Completion Forecast: <EPIC-NAME> (<EPIC-KEY>)', fontsize=14, fontweight='bold')

# Colors
colors = {
    'completed': '#2ecc71',
    'remaining': '#e74c3c',
    'optimistic': '#2ecc71',
    'linear': '#3498db',
    'velocity': '#9b59b6',
    'conservative': '#e67e22'
}

# LEFT: Epic Story Comparison
# RIGHT: Sprint Forecast Scenarios (all 4)

plt.tight_layout()
plt.savefig('<OUTPUT-PATH>', dpi=150, bbox_inches='tight', facecolor='white')
```

### 6. Save Forecast Document

Save markdown report to:
```
forecasts/<epic-name>-forecast.md
```

**Include:**
- Generation date and current sprint
- Reference data summary (project, prefixes, sprints, velocity)
- Target epic summary (stories, filter applied)
- All 4 forecast scenarios in table
- Calculations shown
- Summary with completion sprint estimates
- Assumptions documented

### 7. Present Results

Show the user:

1. **Bottom Line**: X-Y sprints needed, completion Sprint Z

2. **Reference Data Summary**:
   - Reference project (velocity source)
   - Prefixes used
   - Sprint range
   - Stories completed
   - Calculated velocity

3. **Target Epic Summary**:
   - Project: [PRODUCT_PROJECT]
   - Epic key and name
   - Story filter applied
   - Total/Remaining stories

4. **Forecast Scenarios Table**:
   | Scenario | Multiplier | Velocity | Sprints | Target Sprint |
   |----------|------------|----------|---------|---------------|
   | Optimistic | 1.2x | X.XX | X.X | Sprint N |
   | Linear | - | - | X.X | Sprint N |
   | Velocity-Based | 1.0x | X.XX | X.X | Sprint N |
   | Conservative | 0.8x | X.XX | X.X | Sprint N |

5. **Chart Location**: Path to generated PNG

## Output Format

Use clear, scannable markdown with:
- 📊 Bottom line forecast upfront
- 📈 Tables for data and scenarios
- 🎯 All 4 forecast scenarios
- 📉 Chart visualization (always generated)
- 📝 Assumptions and methodology documented

## Key Principles

1. **Reference project for velocity**: Use the reference project's completed stories (defaults to the epic's own project; a separate delivery project is optional)
2. **Target project for the epic**: The epic lives in the target project (`[PRODUCT_PROJECT]` by default)
3. **Prefix filtering**: Only count stories with specified prefixes
4. **1.2x optimistic**: Use 1.2x multiplier for optimistic scenario
5. **Visual output**: Always generate PNG chart
6. **Ask don't assume**: Confirm prefixes and filters with user

## Error Handling

- If no stories match prefix filter, warn user and suggest alternatives
- If the reference project has no matching stories in the sprint range, ask for a different range
- If target epic has no stories, explain scope needs to be defined
- If prefix yields < 5 reference stories, warn about accuracy

## Example Usage

```
User: /forecast-epic

Claude: Which epic do you want to forecast, and which project should I measure velocity from?
User: [PRODUCT_PROJECT]-34 (Example Epic); velocity from the same project

Claude: Which story prefixes should I use for reference velocity?
User: "[Module A] -" and "[Module B] -"

Claude: Which sprint range for reference? (e.g., Sprints 1-6)
User: Sprints 1-6

Claude: For the target epic, should I count ALL stories or filter by prefix?
User: Only "[Module A] -" prefix stories

Claude: What is the current sprint?
User: Sprint 7

Claude: Should I assume 0 stories done, or use actual Jira status?
User: Assume 0 done

Claude: [Fetches reference-project stories with prefixes from Sprints 1-6]
Claude: [Fetches [PRODUCT_PROJECT]-34 stories with "[Module A] -" prefix]
Claude: [Calculates velocity: 16 stories / 6 sprints = 2.67/sprint]
Claude: [Runs 4 scenarios with 1.2x optimistic]
Claude: [Generates PNG chart]
Claude: [Saves markdown report]
Claude: [Presents forecast: 8-16 sprints, Sprint 15-23 completion]
```

## File Outputs

1. **Chart:** `forecasts/<epic-name>-forecast.png`
2. **Report:** `forecasts/<epic-name>-forecast.md`
3. **Script:** `forecasts/generate_forecast_chart.py` (reusable)

## Notes

- This uses story count (# of items), not story points
- Reference velocity based on the reference project's stories with specified prefixes
- Target epic from the target project (`[PRODUCT_PROJECT]` by default), optionally filtered by prefix
- Re-forecast every 2-3 sprints as actuals come in
- 1.2x optimistic multiplier accounts for team learning and improved efficiency
