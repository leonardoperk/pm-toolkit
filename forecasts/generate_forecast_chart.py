import matplotlib.pyplot as plt
import numpy as np

# Set up the figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Epic Completion Forecast: Unified Inbox v1 (RLY-34)', fontsize=14, fontweight='bold')

# Color palette
colors = {
    'completed': '#2ecc71',
    'remaining': '#e74c3c',
    'optimistic': '#2ecc71',
    'velocity': '#9b59b6',
    'conservative': '#e67e22'
}

# ============ LEFT CHART: Epic Story Comparison ============
epics = ['Reference\n(Sprints 1-6)', 'Unified Inbox v1\n(Target)']
completed = [16, 0]
remaining = [0, 33]
totals = [16, 33]

x = np.arange(len(epics))
width = 0.6

# Stacked bar chart
bars1 = ax1.bar(x, completed, width, label='Completed', color=colors['completed'])
bars2 = ax1.bar(x, remaining, width, bottom=completed, label='Remaining', color=colors['remaining'])

ax1.set_ylabel('Number of Stories', fontsize=11)
ax1.set_title('Epic Story Comparison', fontsize=12, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(epics)
ax1.legend(loc='upper left')
ax1.set_ylim(0, 40)

# Add value labels
for i, (comp, rem, total) in enumerate(zip(completed, remaining, totals)):
    if comp > 0:
        ax1.text(i, comp/2, str(comp), ha='center', va='center', color='white', fontweight='bold', fontsize=12)
    if rem > 0:
        ax1.text(i, comp + rem/2, str(rem), ha='center', va='center', color='white', fontweight='bold', fontsize=12)
    ax1.text(i, total + 1, str(total), ha='center', va='bottom', fontweight='bold', fontsize=11)

# ============ RIGHT CHART: Sprint Forecast Scenarios ============
# Linear projection: 6 sprints * (33/16) = 12.4 sprints (same as velocity-based in this case)
scenarios = ['Optimistic\n(1.6x)', 'Linear\nProjection', 'Velocity\nBased', 'Conservative\n(0.8x)']
sprints = [7.7, 12.4, 12.4, 15.5]
scenario_colors = [colors['optimistic'], '#3498db', colors['velocity'], colors['conservative']]

y_pos = np.arange(len(scenarios))
bars = ax2.barh(y_pos, sprints, color=scenario_colors, height=0.6)

ax2.set_xlabel('Estimated Sprints to Complete', fontsize=11)
ax2.set_title('Sprint Forecast Scenarios', fontsize=12, fontweight='bold')
ax2.set_yticks(y_pos)
ax2.set_yticklabels(scenarios)
ax2.set_xlim(0, 18)
ax2.invert_yaxis()

# Add value labels
for i, (bar, sprint) in enumerate(zip(bars, sprints)):
    ax2.text(sprint + 0.3, i, f'{sprint}', va='center', fontweight='bold', fontsize=11, color=scenario_colors[i])

# Add average line
avg_sprints = np.mean(sprints)
ax2.axvline(x=avg_sprints, color='#e74c3c', linestyle='--', linewidth=2, label=f'Average: {avg_sprints:.1f} sprints')

# Add reference line for velocity-based
ax2.axvline(x=12.4, color='#9b59b6', linestyle=':', linewidth=1.5, alpha=0.7)

ax2.legend(loc='lower right', fontsize=9)

# Add sprint number indicators at top
ax2_top = ax2.twiny()
ax2_top.set_xlim(ax2.get_xlim())
sprint_ticks = [7.7, 12.4, 15.5]
sprint_labels = ['Sprint 15', 'Sprint 19', 'Sprint 23']
ax2_top.set_xticks(sprint_ticks)
ax2_top.set_xticklabels(sprint_labels, fontsize=9)
ax2_top.set_xlabel('Target Sprint (from Sprint 7)', fontsize=10)

plt.tight_layout()
plt.savefig('forecasts/unified-inbox-v1-forecast.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print('Chart saved to: forecasts/unified-inbox-v1-forecast.png')
