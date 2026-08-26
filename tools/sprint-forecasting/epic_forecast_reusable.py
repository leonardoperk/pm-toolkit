#!/usr/bin/env python3
"""
Epic Completion Forecast - Reusable Tool
Forecasts epic completion based on historical epic velocity
"""

import argparse
import sys
import numpy as np
import matplotlib.pyplot as plt

def run_epic_forecast(
    reference_epic_name,
    reference_stories_completed,
    reference_sprints_taken,
    target_epic_name,
    target_total_stories,
    target_stories_completed,
    current_sprint,
    historical_throughput=None,
    output_path=None
):
    """
    Run epic completion forecast based on reference epic data

    Args:
        reference_epic_name: Name of completed reference epic
        reference_stories_completed: Number of stories completed in reference epic
        reference_sprints_taken: Number of sprints reference epic took
        target_epic_name: Name of target epic to forecast
        target_total_stories: Total stories in target epic
        target_stories_completed: Stories already completed in target epic
        current_sprint: Current sprint number
        historical_throughput: List of total sprint throughput (optional)
        output_path: Path to save visualization chart (optional)

    Returns:
        dict with forecast results
    """

    # Validate inputs
    if reference_stories_completed < 5:
        print(f"⚠️  Warning: Reference epic has only {reference_stories_completed} stories.")
        print("   Forecast may be less accurate with < 5 stories.")

    if reference_sprints_taken < 1:
        raise ValueError("Reference epic must have taken at least 1 sprint")

    if target_total_stories < 1:
        raise ValueError("Target epic must have at least 1 story")

    # Calculate derived values
    target_stories_remaining = target_total_stories - target_stories_completed
    epic_velocity = reference_stories_completed / reference_sprints_taken
    size_ratio = target_total_stories / reference_stories_completed

    # Calculate team capacity if throughput provided
    if historical_throughput:
        average_total_throughput = np.mean(historical_throughput)
        epic_capacity_ratio = epic_velocity / average_total_throughput
    else:
        average_total_throughput = None
        epic_capacity_ratio = None

    # Print header
    print("=" * 80)
    print(f"EPIC COMPLETION FORECAST: {target_epic_name.upper()}")
    print(f"Based on {reference_epic_name} Historical Data")
    print("=" * 80)

    # Reference epic summary
    print(f"\n📊 {reference_epic_name.upper()} (COMPLETED REFERENCE)")
    print("-" * 80)
    print(f"  Total stories completed: {reference_stories_completed}")
    print(f"  Sprints taken: {reference_sprints_taken}")
    print(f"  Epic velocity: {epic_velocity:.1f} stories/sprint")

    # Target epic summary
    print(f"\n🎯 {target_epic_name.upper()} (TARGET)")
    print("-" * 80)
    print(f"  Total stories: {target_total_stories}")
    print(f"  Completed: {target_stories_completed} stories")
    print(f"  Remaining: {target_stories_remaining} stories")
    print(f"  Current sprint: Sprint {current_sprint}")
    print(f"  Size vs Reference: {size_ratio:.1f}x ({target_total_stories} vs {reference_stories_completed} stories)")

    # Team capacity analysis (if data provided)
    if historical_throughput:
        print(f"\n📈 TEAM CAPACITY ANALYSIS")
        print("-" * 80)
        print(f"  Historical total throughput: {historical_throughput}")
        print(f"  Average total throughput: {average_total_throughput:.1f} items/sprint")
        print(f"  Epic-focused velocity: {epic_velocity:.1f} stories/sprint")
        print(f"  Epic capacity ratio: {epic_capacity_ratio:.1%} of sprint work goes to epic")
        print(f"  Non-epic work: {average_total_throughput - epic_velocity:.1f} items/sprint ({1-epic_capacity_ratio:.1%})")

    # Forecast scenarios
    print(f"\n🔮 FORECAST SCENARIOS")
    print("=" * 80)

    # Scenario 1: Linear projection
    scenario1_sprints = reference_sprints_taken * size_ratio
    scenario1_completion_sprint = current_sprint + scenario1_sprints
    print(f"\n1️⃣  LINEAR PROJECTION (Story Count Ratio)")
    print(f"  Formula: {reference_sprints_taken} sprints × {size_ratio:.2f}x = {scenario1_sprints:.1f} sprints")
    print(f"  Estimated sprints needed: {scenario1_sprints:.1f} sprints")
    print(f"  Expected completion: Sprint {scenario1_completion_sprint:.1f} (~{scenario1_sprints:.0f} sprints from now)")

    # Scenario 2: Velocity-based
    scenario2_sprints = target_stories_remaining / epic_velocity
    scenario2_completion_sprint = current_sprint + scenario2_sprints
    print(f"\n2️⃣  VELOCITY-BASED (Epic Velocity)")
    print(f"  Formula: {target_stories_remaining} remaining stories / {epic_velocity:.1f} stories per sprint")
    print(f"  Estimated sprints needed: {scenario2_sprints:.1f} sprints")
    print(f"  Expected completion: Sprint {scenario2_completion_sprint:.1f} (~{scenario2_sprints:.0f} sprints from now)")

    # Scenario 3: Conservative
    complexity_factor = 0.8
    scenario3_velocity = epic_velocity * complexity_factor
    scenario3_sprints = target_stories_remaining / scenario3_velocity
    scenario3_completion_sprint = current_sprint + scenario3_sprints
    print(f"\n3️⃣  CONSERVATIVE (Complexity Adjusted)")
    print(f"  Adjusted velocity: {scenario3_velocity:.1f} stories/sprint ({complexity_factor:.0%} of baseline)")
    print(f"  Rationale: Accounts for potential higher complexity")
    print(f"  Formula: {target_stories_remaining} stories / {scenario3_velocity:.1f} stories per sprint")
    print(f"  Estimated sprints needed: {scenario3_sprints:.1f} sprints")
    print(f"  Expected completion: Sprint {scenario3_completion_sprint:.1f} (~{scenario3_sprints:.0f} sprints from now)")

    # Scenario 4: Optimistic
    learning_factor = 1.2
    scenario4_velocity = epic_velocity * learning_factor
    scenario4_sprints = target_stories_remaining / scenario4_velocity
    scenario4_completion_sprint = current_sprint + scenario4_sprints
    print(f"\n4️⃣  OPTIMISTIC (Learning Curve)")
    print(f"  Improved velocity: {scenario4_velocity:.1f} stories/sprint ({learning_factor:.0%} of baseline)")
    print(f"  Rationale: Team learns from reference epic, improves efficiency")
    print(f"  Formula: {target_stories_remaining} stories / {scenario4_velocity:.1f} stories per sprint")
    print(f"  Estimated sprints needed: {scenario4_sprints:.1f} sprints")
    print(f"  Expected completion: Sprint {scenario4_completion_sprint:.1f} (~{scenario4_sprints:.0f} sprints from now)")

    # Recommendation
    avg_sprints = np.mean([scenario1_sprints, scenario2_sprints, scenario3_sprints, scenario4_sprints])
    avg_completion_sprint = current_sprint + avg_sprints

    print("\n" + "=" * 80)
    print("💡 RECOMMENDED FORECAST")
    print("=" * 80)
    print(f"\n  Based on averaging all scenarios:")
    print(f"  Estimated sprints needed: {avg_sprints:.1f} sprints (range: {scenario4_sprints:.1f} - {scenario3_sprints:.1f})")
    print(f"  Expected completion: Sprint {avg_completion_sprint:.1f}")
    print(f"  From Sprint {current_sprint} (current): ~{avg_sprints:.0f} more sprints")
    print(f"  Completion sprint range: Sprint {current_sprint + scenario4_sprints:.0f} (optimistic) - Sprint {current_sprint + scenario3_sprints:.0f} (conservative)")

    # Create visualization if output path provided
    if output_path:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        fig.suptitle(f'Epic Completion Forecast: {target_epic_name} vs {reference_epic_name}',
                     fontsize=14, fontweight='bold')

        # Chart 1: Story count comparison
        epics = [f'{reference_epic_name}\n(Completed)', f'{target_epic_name}\n(In Progress)']
        completed = [reference_stories_completed, target_stories_completed]
        remaining = [0, target_stories_remaining]

        x = np.arange(len(epics))
        width = 0.6

        ax1.bar(x, completed, width, label='Completed', color='#2ecc71', edgecolor='black')
        ax1.bar(x, remaining, width, bottom=completed, label='Remaining', color='#e74c3c',
                edgecolor='black', alpha=0.7)

        ax1.set_ylabel('Number of Stories', fontsize=11, fontweight='bold')
        ax1.set_title('Epic Story Comparison', fontsize=12, fontweight='bold')
        ax1.set_xticks(x)
        ax1.set_xticklabels(epics)
        ax1.legend()
        ax1.grid(axis='y', alpha=0.3)

        # Add value labels
        for i, (comp, rem) in enumerate(zip(completed, remaining)):
            total = comp + rem
            ax1.text(i, total + max(total * 0.05, 1), f'{total}', ha='center', va='bottom', fontweight='bold')
            if comp > 0:
                ax1.text(i, comp/2, f'{comp}', ha='center', va='center', color='white', fontweight='bold')
            if rem > 0:
                ax1.text(i, comp + rem/2, f'{rem}', ha='center', va='center', color='white', fontweight='bold')

        # Chart 2: Sprint forecast scenarios
        scenarios = ['Linear\nProjection', 'Velocity\nBased', 'Conservative\n(Complexity)', 'Optimistic\n(Learning)']
        sprint_estimates = [scenario1_sprints, scenario2_sprints, scenario3_sprints, scenario4_sprints]
        colors = ['#3498db', '#9b59b6', '#e67e22', '#2ecc71']

        bars = ax2.barh(scenarios, sprint_estimates, color=colors, edgecolor='black', alpha=0.8)
        ax2.axvline(x=avg_sprints, color='red', linestyle='--', linewidth=2,
                   label=f'Average: {avg_sprints:.1f} sprints')
        ax2.axvline(x=reference_sprints_taken, color='gray', linestyle=':', linewidth=2,
                   label=f'{reference_epic_name}: {reference_sprints_taken} sprints')

        ax2.set_xlabel('Estimated Sprints to Complete', fontsize=11, fontweight='bold')
        ax2.set_title('Sprint Forecast Scenarios', fontsize=12, fontweight='bold')
        ax2.legend(loc='lower right')
        ax2.grid(axis='x', alpha=0.3)

        # Add value labels on bars
        for i, (bar, val) in enumerate(zip(bars, sprint_estimates)):
            ax2.text(val + 0.2, bar.get_y() + bar.get_height()/2,
                    f'{val:.1f}', va='center', fontweight='bold')

        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        print(f"\n📊 Chart saved to: {output_path}")

    # Key insights
    print("\n" + "=" * 80)
    print("🔑 KEY INSIGHTS")
    print("=" * 80)
    print(f"\n1. {target_epic_name} is {size_ratio:.1f}x {'larger' if size_ratio > 1 else 'smaller'} than {reference_epic_name}")
    print(f"   ({target_total_stories} stories vs {reference_stories_completed} stories)")

    if historical_throughput:
        print(f"\n2. Team dedicates ~{epic_capacity_ratio:.0%} of sprint capacity to epic work")
        print(f"   Epic velocity: {epic_velocity:.1f} stories/sprint")
        print(f"   Total throughput: {average_total_throughput:.1f} items/sprint")

    print(f"\n3. At current velocity ({epic_velocity:.1f} stories/sprint):")
    print(f"   {target_stories_remaining} remaining stories → ~{scenario2_sprints:.0f} sprints needed")

    print(f"\n4. Forecast range: {scenario4_sprints:.0f}-{scenario3_sprints:.0f} sprints")
    print(f"   Best case (optimistic): {scenario4_sprints:.0f} sprints → Sprint {current_sprint + scenario4_sprints:.0f}")
    print(f"   Worst case (conservative): {scenario3_sprints:.0f} sprints → Sprint {current_sprint + scenario3_sprints:.0f}")
    print(f"   Most likely (average): {avg_sprints:.0f} sprints → Sprint {current_sprint + avg_sprints:.0f}")

    print("\n" + "=" * 80)

    # Return results
    return {
        'reference_epic': {
            'name': reference_epic_name,
            'stories': reference_stories_completed,
            'sprints': reference_sprints_taken,
            'velocity': epic_velocity
        },
        'target_epic': {
            'name': target_epic_name,
            'total_stories': target_total_stories,
            'completed': target_stories_completed,
            'remaining': target_stories_remaining,
            'size_ratio': size_ratio
        },
        'scenarios': {
            'linear': scenario1_sprints,
            'velocity_based': scenario2_sprints,
            'conservative': scenario3_sprints,
            'optimistic': scenario4_sprints,
            'average': avg_sprints
        },
        'completion_sprints': {
            'optimistic': current_sprint + scenario4_sprints,
            'average': current_sprint + avg_sprints,
            'conservative': current_sprint + scenario3_sprints
        }
    }


def main():
    parser = argparse.ArgumentParser(
        description='Epic completion forecast based on historical epic velocity'
    )

    parser.add_argument('--reference-name', type=str, required=True,
                       help='Name of completed reference epic (e.g., "Broadcast Campaigns v1")')
    parser.add_argument('--reference-stories', type=int, required=True,
                       help='Number of stories completed in reference epic')
    parser.add_argument('--reference-sprints', type=int, required=True,
                       help='Number of sprints reference epic took')

    parser.add_argument('--target-name', type=str, required=True,
                       help='Name of target epic to forecast (e.g., "Unified Inbox")')
    parser.add_argument('--target-total', type=int, required=True,
                       help='Total number of stories in target epic')
    parser.add_argument('--target-completed', type=int, default=0,
                       help='Number of stories already completed in target epic (default: 0)')

    parser.add_argument('--current-sprint', type=int, required=True,
                       help='Current sprint number')

    parser.add_argument('--throughput', nargs='+', type=int,
                       help='Historical sprint throughput (space-separated, optional)')

    parser.add_argument('--output', '-o', type=str,
                       help='Path to save chart image (optional)')

    args = parser.parse_args()

    try:
        results = run_epic_forecast(
            reference_epic_name=args.reference_name,
            reference_stories_completed=args.reference_stories,
            reference_sprints_taken=args.reference_sprints,
            target_epic_name=args.target_name,
            target_total_stories=args.target_total,
            target_stories_completed=args.target_completed,
            current_sprint=args.current_sprint,
            historical_throughput=args.throughput,
            output_path=args.output
        )
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
