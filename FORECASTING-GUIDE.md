# Forecasting Guide - Standard Process

This guide explains the standardized forecasting processes available in the PM Toolkit. Use these data-driven forecasting tools to set realistic expectations and make informed planning decisions.

---

## Overview

Two complementary forecasting tools are available:

| Tool | Purpose | Timeframe | Command |
|------|---------|-----------|---------|
| **Sprint Forecast** | Probability of completing current sprint | 1-2 weeks | `/forecast-sprint` |
| **Epic Forecast** | Number of sprints to complete an epic | 2-6 months | `/forecast-epic` |

Both tools use historical Jira data and probabilistic modeling to provide evidence-based forecasts.

---

## When to Use Each Tool

### Use `/forecast-sprint` when:
✅ Planning or mid-sprint: "Can we finish this sprint?"
✅ Sprint scope concerns: "Should we descope?"
✅ Capacity check: "Can we take on more work?"
✅ Stakeholder update: "What's our completion confidence?"

**Frequency:** Run at sprint start, mid-sprint, and when scope changes

### Use `/forecast-epic` when:
✅ Epic planning: "How long will this take?"
✅ Roadmap planning: "When will this be done?"
✅ Scope evaluation: "Is this too big?"
✅ Descoping decisions: "What can move to v2?"
✅ Progress check: "Are we on track?" (re-forecast every 2-3 sprints)

**Frequency:** Run at epic kickoff, then every 2-3 sprints to validate

---

## Sprint Forecasting Process

### Standard Workflow

1. **Trigger the forecast:**
   ```
   /forecast-sprint
   ```

2. **Provide information** (Claude will ask):
   - Which sprint to forecast (e.g., "Sprint 6")
   - Number of historical sprints to analyze (default: 4, recommended: 4-6)
   - Simulation thoroughness (default: 10,000 runs, recommended)

3. **Review results:**
   - Completion probability (e.g., 75%)
   - Confidence level (🟢 High / 🟡 Moderate / 🔴 Low)
   - Percentile analysis
   - Distribution chart
   - Risk factors

4. **Take action based on probability:**
   - **≥85% (🟢 High):** On track, no action needed
   - **70-84% (🟡 Moderate-High):** Slight risk, monitor closely
   - **50-69% (🟠 Moderate):** Significant risk, consider descoping
   - **<50% (🔴 Low):** Will not complete, descope required

### Best Practices

- **Timing:** Run at sprint start and mid-sprint
- **History:** Use 4-6 recent sprints for best accuracy
- **Consistency:** Use same project and issue types (Stories + Bugs)
- **Updates:** Re-run if scope changes significantly
- **Communication:** Share probability with team and stakeholders

### Example Decision Tree

```
Sprint Forecast: 65% probability
         ↓
  🟠 MODERATE risk
         ↓
    Options:
    1. Descope lowest priority 2-3 items
    2. Extend sprint by 1-2 days (if possible)
    3. Add team capacity (if available)
    4. Accept 35% risk of incomplete sprint
```

---

## Epic Forecasting Process

### Standard Workflow

1. **Trigger the forecast:**
   ```
   /forecast-epic
   ```

2. **Provide information** (Claude will ask):
   - Target epic to forecast (Jira key or URL, e.g., "[PRODUCT_PROJECT]-34")
   - Completed reference epic (Jira key or URL, e.g., "[PRODUCT_PROJECT]-40")
   - Current sprint number (e.g., "Sprint 5")

3. **Review results:**
   - Sprint estimate (e.g., 7-8 sprints)
   - Completion sprint range (e.g., Sprint 11-14)
   - Four scenarios (optimistic, velocity-based, linear, conservative)
   - Size comparison (e.g., 1.6x larger than reference)
   - Team capacity analysis (e.g., 38% of sprint on epic work)
   - Milestone checkpoints
   - Descoping recommendations

4. **Take action based on forecast:**
   - Set realistic deadline expectations
   - Add buffer sprints for risk
   - Identify descoping candidates (20-30% of scope)
   - Plan milestone checkpoints
   - Communicate timeline to stakeholders

### Best Practices

- **Reference selection:** Use recently completed epic (< 6 months old)
- **Similarity:** Choose reference epic from similar domain/technology
- **Scope definition:** Target epic should have most stories defined
- **Re-forecasting:** Update every 2-3 sprints with actual velocity
- **Checkpoints:** Review at suggested milestones (25%, 50%, 75%)
- **Buffer planning:** Add 1-2 sprint buffer to conservative scenario

### Example Planning Timeline

```
Sprint 5: Run epic forecast
         ↓
    Result: 7-8 sprints needed
         ↓
Sprint 7: First checkpoint (25%)
         ↓
    Check: Did we complete ~8 stories as expected?
         ↓
Sprint 9: Mid-point review (50%)
         ↓
    Decision: Descope if behind target
         ↓
Sprint 11: Final push (75%)
         ↓
    Plan: Lock scope for final 2 sprints
         ↓
Sprint 13: Target completion
```

---

## Integration & Automation

### Jira Integration

Both tools automatically fetch data from Jira:
- Sprint stories and status
- Epic stories and completion
- Historical throughput
- No manual data entry required

### Artifacts Generated

Each forecast creates standardized artifacts:

**Sprint Forecast:**
- `tools/sprint-forecasting/outputs/sprint-X-forecast.png` - Distribution chart
- `projects/sprint-forecasts/sprint-X-summary.md` - Detailed report (optional)

**Epic Forecast:**
- `tools/sprint-forecasting/outputs/<epic-name>-forecast.png` - Comparison chart
- `projects/sprint-forecasts/<epic-name>-forecast-summary.md` - Detailed report with recommendations

### Sharing Results

**With Team:**
- Share completion probability at standup
- Post chart in team Slack channel
- Reference in sprint retrospectives

**With Stakeholders:**
- Include in status reports
- Use for roadmap planning conversations
- Support deadline negotiations with data

**With Leadership:**
- Portfolio planning and capacity discussions
- Risk assessment for key initiatives
- Resource allocation decisions

---

## Combining Both Tools

Use both tools together for comprehensive planning:

### Example: New Epic Planning

1. **Epic Forecast** → 8 sprints needed (Sprint 5 → Sprint 13)
2. **Sprint Forecast** (each sprint):
   - Sprint 6: 80% probability → On track
   - Sprint 7: 65% probability → Descope 2 items
   - Sprint 8: 75% probability → Back on track
   - Sprint 9: Re-run **Epic Forecast** → Adjust to 9 sprints
   - Sprint 10-13: Continue monitoring

### Quarterly Planning Workflow

```
Quarter Start:
├─ Epic 1: /forecast-epic → 5 sprints (Sprint 1-5)
├─ Epic 2: /forecast-epic → 8 sprints (Sprint 6-13)
└─ Epic 3: /forecast-epic → 6 sprints (Sprint 14-19)

Each Sprint:
└─ /forecast-sprint → Monitor current sprint completion

Mid-Epic:
└─ /forecast-epic (re-run) → Validate timeline
```

---

## Key Principles

### 1. Data-Driven Decisions
- Use actual historical data, not estimates or gut feel
- Let probability guide planning decisions
- Update forecasts as new data becomes available

### 2. Probabilistic Thinking
- No forecast is 100% certain
- Plan for range of outcomes (optimistic → conservative)
- Add appropriate buffers based on confidence level

### 3. Transparent Communication
- Share probability and range with stakeholders
- Explain assumptions and limitations
- Update regularly as situation changes

### 4. Continuous Improvement
- Compare forecast vs actual outcomes
- Refine assumptions based on results
- Adjust descoping strategies over time

### 5. Actionable Insights
- Every forecast should lead to a decision
- Use checkpoints to validate assumptions
- Re-forecast when velocity differs from expected

---

## Common Pitfalls & Solutions

### Pitfall 1: First Sprint/Epic (No Historical Data)
**Solution:** Wait until 2-3 sprints complete, or use external benchmarks with large uncertainty buffer

### Pitfall 2: Major Team Changes
**Solution:** Historical data may not apply; reset baseline after team stabilizes

### Pitfall 3: Scope Creep During Sprint/Epic
**Solution:** Re-run forecast after scope changes to update probability/timeline

### Pitfall 4: Treating Forecast as Commitment
**Solution:** Forecast is probability, not promise; communicate as range with confidence level

### Pitfall 5: Ignoring Low Probability
**Solution:** Act on forecast - descope, add capacity, or extend timeline

### Pitfall 6: One-Time Forecast
**Solution:** Re-forecast regularly (sprint: mid-sprint, epic: every 2-3 sprints)

---

## Metrics & KPIs

Track forecast accuracy over time:

### Sprint Forecast Accuracy
- **Target:** 80%+ forecasts match actual outcomes
- **Measure:** Compare predicted probability to actual completion
- **Improvement:** Adjust number of historical sprints analyzed

### Epic Forecast Accuracy
- **Target:** Actual completion within forecast range (optimistic → conservative)
- **Measure:** Compare predicted sprints to actual sprints taken
- **Improvement:** Refine complexity factors, improve story estimation

### Forecast Usage
- **Target:** 100% of sprints/epics have at least one forecast
- **Measure:** Count forecasts vs sprints/epics
- **Improvement:** Integrate into standard planning process

---

## Advanced Techniques

### Segmented Forecasting
Run separate forecasts for different work types:
- Stories only (new features)
- Bugs only (maintenance work)
- Technical debt (infrastructure work)

### Confidence Intervals
For critical deadlines, use conservative scenario + additional buffer:
- Conservative forecast: 9 sprints
- Buffer: +2 sprints
- Committed deadline: 11 sprints (95%+ confidence)

### Velocity Trending
Track epic velocity over multiple epics:
- Epic 1: 4.2 stories/sprint
- Epic 2: 4.8 stories/sprint (improving!)
- Epic 3 forecast: Use 4.5 stories/sprint (average)

---

## Templates & Checklists

### Sprint Planning Checklist
- [ ] Run `/forecast-sprint` at sprint start
- [ ] Review probability with team
- [ ] Identify descoping candidates if <75%
- [ ] Document forecast in sprint goals
- [ ] Re-forecast mid-sprint if scope changes
- [ ] Compare forecast vs actual at retrospective

### Epic Planning Checklist
- [ ] Define all stories before forecasting
- [ ] Select comparable completed reference epic
- [ ] Run `/forecast-epic`
- [ ] Add buffer sprints (1-2) to conservative scenario
- [ ] Identify 20-30% descoping candidates
- [ ] Set milestone checkpoints (25%, 50%, 75%)
- [ ] Communicate timeline range to stakeholders
- [ ] Re-forecast every 2-3 sprints
- [ ] Adjust scope/timeline at checkpoints

---

## Getting Help

### Documentation
- **Sprint Forecast:** `tools/sprint-forecasting/README.md` (Sprint section)
- **Epic Forecast:** `tools/sprint-forecasting/README.md` (Epic section)
- **Commands:** `.claude/commands/forecast-sprint.md` and `.claude/commands/forecast-epic.md`

### Command Reference
```bash
# Slash commands (recommended)
/forecast-sprint
/forecast-epic

# Direct script usage (advanced)
python3 tools/sprint-forecasting/monte_carlo_forecast.py --help
python3 tools/sprint-forecasting/epic_forecast_reusable.py --help
```

### Troubleshooting
- Check Jira connection if data fetch fails
- Verify Python dependencies: `pip3 install numpy matplotlib`
- Ensure sufficient historical data (2+ sprints/epics)
- Re-authenticate Jira if auth expires

---

**Last Updated:** January 28, 2026
**Version:** 1.0
**Maintainer:** PM Toolkit
**Feedback:** Share improvements via team retros or GitHub issues
