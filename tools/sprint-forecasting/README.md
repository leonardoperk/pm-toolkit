# Sprint & Epic Forecasting Tools

Probabilistic forecasting tools for sprint completion and epic duration based on historical data.

## Tools Included

1. **Sprint Forecast** - Monte Carlo simulation for sprint completion probability
2. **Epic Forecast** - Epic duration forecast based on historical epic velocity

## What It Does

Uses historical throughput data to forecast the probability of completing a target sprint. The tool:
- Samples randomly from past sprint performance
- Runs 10,000+ simulations
- Calculates completion probability
- Generates percentile analysis
- Creates visual distribution charts

## How to Use

### Via Slash Command (Recommended)

```
/forecast-sprint
```

Claude will:
1. Ask which sprint to forecast
2. Fetch historical data from Jira automatically
3. Run the simulation
4. Present results with chart and insights

### Direct Script Usage

```bash
python3 tools/sprint-forecasting/monte_carlo_forecast.py [THROUGHPUT...] --remaining N [OPTIONS]
```

**Arguments:**
- `THROUGHPUT...`: Space-separated integers (historical items completed per sprint)
- `--remaining N`, `-r N`: Items remaining in target sprint (required)
- `--sprint-name NAME`, `-s NAME`: Sprint name (default: "Sprint")
- `--simulations N`, `-n N`: Number of runs (default: 10,000)
- `--output PATH`, `-o PATH`: Path to save chart (optional)

**Example:**
```bash
# Forecast Sprint 6 with 8 remaining items
# Based on throughput: Sprint 2=4, Sprint 3=9, Sprint 4=11, Sprint 5=7
python3 tools/sprint-forecasting/monte_carlo_forecast.py 4 9 11 7 \
  --remaining 8 \
  --sprint-name "Sprint 6" \
  --output outputs/sprint6-forecast.png
```

## Output

The tool provides:

1. **Probability Percentage**: X% chance of completing all items
2. **Confidence Level**: 🟢 High / 🟡 Moderate-High / 🟠 Moderate / 🔴 Low
3. **Historical Stats**: Average, std dev, min, max throughput
4. **Percentile Analysis**: P50, P75, P85, P95 projections
5. **Distribution Chart**: Visual showing completion probability
6. **Key Insights**: Actionable recommendations

## Methodology

**Monte Carlo Simulation:**
1. Collect historical throughput (completed items per sprint)
2. For each simulation run:
   - Randomly sample one sprint's throughput
   - Check if it completes all remaining items
3. Calculate probability as: (successes / total runs) × 100

**Assumptions:**
- Work complexity is similar across sprints
- Team capacity remains consistent
- Historical patterns will continue

**Limitations:**
- Requires at least 2 historical sprints (4+ recommended)
- Doesn't account for scope changes mid-sprint
- Uses item count, not story points

## Confidence Levels

| Probability | Level | Emoji | Meaning |
|-------------|-------|-------|---------|
| ≥85% | HIGH | 🟢 | Very likely to complete |
| 70-84% | MODERATE-HIGH | 🟡 | Good chance |
| 50-69% | MODERATE | 🟠 | About 50/50 |
| <50% | LOW | 🔴 | Unlikely to complete |

## File Organization

Forecasts are saved to:
```
projects/sprint-forecasts/
├── sprint-5-forecast.py      # Script with embedded data
└── sprint-5-summary.md        # Optional markdown summary

outputs/
└── sprint-5-forecast.png      # Distribution chart
```

## Dependencies

```bash
pip3 install numpy matplotlib
```

Already installed if you set up Phase 1 skills.

## When to Use

**Good use cases:**
- Sprint planning: "Can we commit to this scope?"
- Mid-sprint check-ins: "Are we on track?"
- Capacity planning: "How much can we take on?"
- Risk assessment: "What's our completion confidence?"

**Not ideal for:**
- First sprint (no historical data)
- Major team changes (capacity shifts)
- Wildly different work types (compare apples to apples)

## Tips for Best Results

1. **Use consistent data**: Same team, same project, same issue types
2. **More history = better**: 4+ sprints recommended
3. **Run mid-sprint**: Update forecast as sprint progresses
4. **Segment by type**: Can run separately for Stories vs Bugs if needed
5. **Check assumptions**: Verify work complexity is comparable

## Example Output

```
✨ PROBABILITY OF COMPLETING ALL SPRINT 5 ITEMS: 75.4%

Throughput Percentiles:
  P50 (50th percentile): 9 items
  P75 (75th percentile): 11 items
  P85 (85th percentile): 11 items
  P95 (95th percentile): 11 items

Confidence level: 🟡 MODERATE-HIGH - Good chance of completion
```

## Integration with Jira

The `/forecast-sprint` command automatically:
- Fetches completed items from historical sprints
- Retrieves target sprint scope
- Calculates remaining work
- No manual data entry required

## Troubleshooting

**"Need at least 2 historical sprints"**
- Run at least 2 sprints before forecasting
- Can't forecast without historical data

**"ModuleNotFoundError: numpy"**
```bash
pip3 install numpy matplotlib
```

**"Sprint must have at least 1 remaining item"**
- Forecast only works if there's work left to do
- If sprint is complete, probability is 100%

**Chart not displaying**
- Check file was saved to outputs/ folder
- View with: `open outputs/sprint-X-forecast.png`

---

# Epic Forecasting Tool

Forecast epic completion timeline based on historical epic velocity and story count comparison.

## What It Does

Uses completed epic data to forecast how many sprints a new epic will take. The tool:
- Compares target epic size to a reference epic
- Calculates epic velocity from historical data
- Analyzes team capacity allocation
- Generates 4 forecast scenarios (linear, velocity-based, conservative, optimistic)
- Creates comparative visualizations
- Provides milestone checkpoints and descoping recommendations

## How to Use

### Via Slash Command (Recommended)

```
/forecast-epic
```

Claude will:
1. Ask for target epic and reference epic (keys or URLs)
2. Fetch epic data and all stories from Jira
3. Calculate epic velocity and size comparison
4. Run 4 forecast scenarios
5. Present results with chart, insights, and recommendations

### Direct Script Usage

```bash
python3 tools/sprint-forecasting/epic_forecast_reusable.py \
  --reference-name "Epic Name" \
  --reference-stories N \
  --reference-sprints N \
  --target-name "Target Epic" \
  --target-total N \
  --target-completed N \
  --current-sprint N \
  [--throughput N N N...] \
  [--output PATH]
```

**Arguments:**
- `--reference-name`: Name of completed reference epic (required)
- `--reference-stories`: Stories completed in reference epic (required)
- `--reference-sprints`: Sprints reference epic took (required)
- `--target-name`: Name of target epic to forecast (required)
- `--target-total`: Total stories in target epic (required)
- `--target-completed`: Stories already done (default: 0)
- `--current-sprint`: Current sprint number (required)
- `--throughput`: Historical sprint throughput (optional, enables capacity analysis)
- `--output`: Path to save chart (optional)

**Example:**
```bash
python3 tools/sprint-forecasting/epic_forecast_reusable.py \
  --reference-name "[Reference Epic] v1" \
  --reference-stories 21 \
  --reference-sprints 5 \
  --target-name "[Target Epic]" \
  --target-total 33 \
  --target-completed 2 \
  --current-sprint 5 \
  --throughput 4 9 19 12 \
  --output outputs/unified-inbox-forecast.png
```

## Output

The tool provides:

1. **Sprint Estimate**: X-Y sprints needed (range and average)
2. **Completion Sprint**: Expected completion sprint number
3. **Reference Epic Summary**: Velocity and duration of completed epic
4. **Target Epic Analysis**: Size comparison and remaining work
5. **Team Capacity Breakdown**: Epic work vs other work allocation
6. **Four Scenarios**: Linear, velocity-based, conservative, optimistic
7. **Visualization Chart**: Story comparison and scenario breakdown
8. **Key Insights**: Size ratio, capacity analysis, risk factors
9. **Recommendations**: Target planning, checkpoints, descoping options

## Forecast Scenarios

The tool generates 4 scenarios to provide a range of estimates:

### 1️⃣ Linear Projection
- **Formula:** Reference sprints × (Target stories / Reference stories)
- **Use when:** Epics have similar complexity
- **Assumption:** Work scales linearly with story count

### 2️⃣ Velocity-Based
- **Formula:** Remaining stories / Epic velocity
- **Use when:** Team composition and velocity are stable
- **Assumption:** Historical epic velocity continues

### 3️⃣ Conservative (Complexity Adjusted)
- **Formula:** Remaining stories / (Epic velocity × 0.8)
- **Use when:** Target epic is more complex or described as "much bigger"
- **Assumption:** 20% slower velocity due to complexity

### 4️⃣ Optimistic (Learning Curve)
- **Formula:** Remaining stories / (Epic velocity × 1.2)
- **Use when:** Team has learned from reference epic
- **Assumption:** 20% faster velocity due to experience

## Methodology

**Epic Velocity Calculation:**
1. Count stories completed in reference epic
2. Count sprints reference epic took
3. Epic velocity = Stories / Sprints

**Capacity Analysis (Optional):**
1. Fetch historical total sprint throughput
2. Calculate: Epic capacity ratio = Epic velocity / Total throughput
3. Shows % of sprint dedicated to epic work vs other work (bugs, support, etc.)

**Forecasting:**
1. Calculate size ratio: Target stories / Reference stories
2. Run 4 scenarios with different velocity assumptions
3. Average scenarios for recommended forecast
4. Generate completion sprint range (optimistic → conservative)

**Assumptions:**
- Stories are relatively comparable in size/complexity
- Team capacity remains consistent
- Reference epic is representative of future work
- No major process or team changes

**Limitations:**
- Requires completed reference epic (minimum 5 stories recommended)
- Assumes similar work domain and technical stack
- Story count may not reflect true complexity differences
- Single reference epic provides limited historical data

## When to Use

**Good use cases:**
- Planning new epic based on recently completed similar epic
- Setting deadline expectations with stakeholders
- Evaluating epic scope against team capacity
- Deciding whether to descope before starting
- Mid-epic re-forecasting based on actual progress

**Not ideal for:**
- No comparable completed epic exists
- Epic has < 5 stories defined
- Completely different work domain or technology
- Major team composition changes since reference epic

## Example Output

```
🎯 UNIFIED INBOX (TARGET)
  Total stories: 33
  Remaining: 31 stories
  Size vs Reference: 1.6x larger

📈 TEAM CAPACITY ANALYSIS
  Epic velocity: 4.2 stories/sprint
  Epic capacity ratio: 38% of sprint work goes to epic

💡 RECOMMENDED FORECAST
  Estimated sprints needed: 7.7 sprints (range: 6.2 - 9.2)
  Expected completion: Sprint 13
  Completion range: Sprint 11 (optimistic) - Sprint 14 (conservative)
```

## Milestone Checkpoints

The tool automatically suggests checkpoints for tracking progress:

| Sprint | Checkpoint | % Complete | Purpose |
|--------|------------|------------|---------|
| +2 | Early checkpoint | 25-30% | Early velocity validation |
| +4 | Mid-point review | 50% | Make descope decisions |
| +6 | Final push | 75% | Confirm last stories |
| +8 | Target completion | 100% | Planned finish |

## Descoping Strategy

The tool recommends identifying 20-30% of stories as potential v2 candidates:

**Good descoping candidates:**
- Nice-to-have features
- Research or spike stories
- Separate feature areas
- Enhancements vs core functionality
- Low user impact items

**Keep in v1:**
- Core functionality
- Must-haves for minimum viable epic
- High user/business impact
- Dependencies for other work

## File Organization

Forecasts are saved to:
```
projects/sprint-forecasts/
├── <epic-name>-forecast-summary.md    # Detailed report
└── <epic-name>-forecast.py            # Script with embedded data (if generated)

tools/sprint-forecasting/outputs/
└── <epic-name>-forecast.png           # Visualization chart
```

## Integration with Jira

The `/forecast-epic` command automatically:
- Fetches epic metadata (status, dates, description)
- Retrieves all child stories/bugs
- Counts completed vs remaining work
- Calculates size comparison
- Uses sprint throughput data for capacity analysis
- No manual counting required

## Tips for Best Results

1. **Choose recent reference**: Use recently completed epic (< 6 months old)
2. **Similar domain**: Compare similar types of work (feature vs feature, infrastructure vs infrastructure)
3. **Same team**: Reference epic should be from same team composition
4. **Complete epic**: Reference epic must be fully done, not partially complete
5. **Define scope**: Target epic should have most/all stories defined upfront
6. **Re-forecast**: Update forecast every 2-3 sprints with actual velocity
7. **Use checkpoints**: Review at suggested milestones and adjust

## Example Workflow

1. **Sprint 1**: Complete Epic A (21 stories, 5 sprints)
2. **Sprint 5**: Plan Epic B (33 stories)
3. **Run forecast**:
   ```
   /forecast-epic
   Reference: Epic A ([PRODUCT_PROJECT]-40)
   Target: Epic B ([PRODUCT_PROJECT]-34)
   ```
4. **Get results**: 7-8 sprints, completion Sprint 12-13
5. **Sprint 7**: First checkpoint - validate velocity
6. **Sprint 9**: Mid-point review - make descope decisions if needed
7. **Sprint 11**: Final push - confirm last stories
8. **Sprint 13**: Target completion

## Troubleshooting

**"Reference epic has only X stories. Forecast may be less accurate."**
- Ideally use reference epic with 10+ stories
- Small epics (< 5 stories) provide limited data
- Consider using average of multiple completed epics

**"Target epic has no stories yet"**
- Define epic scope first (create stories/bugs)
- Forecast requires knowing target size
- Can run rough estimate with story count guess

**Forecast seems off after few sprints**
- Re-run forecast with actuals
- Adjust complexity factor if velocity different than expected
- May need to descope if significantly behind

**Reference and target epics very different**
- Warning: Forecast may be inaccurate
- Consider finding more comparable reference
- Or adjust complexity factor manually

---

**Created:** January 26-28, 2026
**Based on:** Historical epic velocity and Monte Carlo simulation methodologies
**Part of:** PM Toolkit Phase 2 - Custom Skills & Slash Commands
