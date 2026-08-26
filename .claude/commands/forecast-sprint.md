---
description: "Monte Carlo sprint completion forecast using historical throughput"
---

# Sprint Completion Forecast Command

You are executing the `/forecast-sprint` command to perform a Monte Carlo simulation that forecasts the probability of completing a target sprint based on historical throughput data.

## Workflow

### 1. Gather Information

Use AskUserQuestion to collect:
- **Target sprint number** (the sprint to forecast)
- **Number of historical sprints** to analyze (default: 4, min: 2, max: 10)
- **Simulation runs** (Quick: 1,000 / Standard: 10,000 / Thorough: 50,000)

**Example questions:**
```
Which sprint do you want to forecast? (e.g., "Sprint 6")
How many previous sprints should I analyze for historical throughput? (default: 4)
How thorough should the simulation be? (Standard: 10,000 runs recommended)
```

### 2. Fetch Historical Data from Jira

For each historical sprint (e.g., if forecasting Sprint 6, analyze Sprints 2-5):

```jql
project = [ENG_PROJECT] AND type = Story AND sprint = "Sprint X" AND status = Done
```

Count the completed stories for each sprint to build the throughput distribution.

**Important:** Only count Stories that reached "Done" status. Do NOT include Bugs.

### 3. Fetch Target Sprint Scope

Query the target sprint to get total scope:

```jql
project = [ENG_PROJECT] AND type = Story AND sprint = "Sprint X"
```

Separate into:
- Stories already Done
- Stories still To Do / In Progress / In Review

Calculate remaining stories to complete.

### 4. Run Monte Carlo Simulation

Use the Python script at `tools/sprint-forecasting/monte_carlo_forecast.py`:

**Pass parameters:**
- Historical throughput array (e.g., [4, 9, 11, 7])
- Target sprint remaining items (e.g., 6)
- Number of simulation runs (e.g., 10,000)

**The script will:**
- Randomly sample from historical throughput distribution
- Count how many simulations complete all remaining items
- Calculate completion probability
- Generate percentile analysis
- Create visualization chart

### 5. Present Results

Show the user:

1. **Bottom Line**: X% probability of completing Sprint Y

2. **Data Summary**:
   - Historical throughput table (per sprint)
   - Average, min, max, std deviation
   - Target sprint scope (total, done, remaining)

3. **Simulation Results**:
   - Probability percentage
   - Confidence level (High/Moderate/Low)
   - Percentile breakdown (P50, P75, P85, P95)
   - Distribution chart

4. **Key Insights**:
   - What the team needs to complete
   - How historical average compares to target
   - Risk factors (variability, underperformance scenarios)

5. **Recommendations**:
   - Prioritization suggestions
   - Risk mitigation strategies
   - When to escalate or descope

### 6. Save Artifacts

Save the following to `projects/sprint-forecasts/`:
- Python script with embedded data: `sprint-X-forecast.py`
- Chart image: `outputs/sprint-X-forecast.png`
- Summary report (optional): `projects/sprint-forecasts/sprint-X-summary.md`

## Output Format

Use clear, scannable markdown with:
- 🎯 Bottom line probability upfront
- 📊 Tables for data
- 🟢🟡🔴 Color-coded confidence levels
- 💡 Actionable insights
- Visual chart included

## Key Principles

1. **Data-driven**: Use actual Jira data, not estimates
2. **Transparent**: Show historical distribution and variability
3. **Actionable**: Provide recommendations based on probability
4. **Visual**: Always include the distribution chart
5. **Honest**: Acknowledge risks and limitations

## Confidence Levels

- **🟢 HIGH** (≥85%): Very likely to complete
- **🟡 MODERATE-HIGH** (70-84%): Good chance of completion
- **🟠 MODERATE** (50-69%): About 50/50
- **🔴 LOW** (<50%): Unlikely to complete all items

## Error Handling

- If historical data is insufficient (< 2 sprints), warn user
- If target sprint has no scope yet, explain we need committed items
- If Jira connection fails, provide clear error message
- If Python dependencies missing, install numpy and matplotlib

## Example Usage

```
User: /forecast-sprint
Claude: [Asks questions via AskUserQuestion]
Claude: [Fetches Jira data from sprints 2-5]
Claude: [Runs simulation]
Claude: [Presents 75% probability with chart and insights]
```

## Notes

- This uses throughput (count of Stories only, no Bugs), not story points
- Simulation assumes similar work complexity across sprints
- More historical data = more accurate forecast
- Chart is saved to outputs/ folder
- Can be run mid-sprint to check progress
