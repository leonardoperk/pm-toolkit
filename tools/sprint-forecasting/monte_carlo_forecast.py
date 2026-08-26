#!/usr/bin/env python3
"""
Monte Carlo Simulation for Sprint Completion Forecast
Reusable utility for forecasting sprint completion probability
"""

import argparse
import sys
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def run_forecast(historical_throughput, sprint_remaining, sprint_name="Sprint",
                 num_simulations=10_000, output_path=None):
    """
    Run Monte Carlo simulation for sprint completion forecast

    Args:
        historical_throughput: List of integers (items completed per sprint)
        sprint_remaining: Integer (items remaining to complete)
        sprint_name: String (name of sprint being forecasted)
        num_simulations: Integer (number of simulation runs)
        output_path: String (path to save chart, or None)

    Returns:
        dict with results: probability, percentiles, distribution, insights
    """

    # Validate inputs
    if len(historical_throughput) < 2:
        raise ValueError("Need at least 2 historical sprints for meaningful forecast")
    if sprint_remaining < 1:
        raise ValueError("Sprint must have at least 1 remaining item")

    # Calculate historical stats
    avg_throughput = np.mean(historical_throughput)
    std_throughput = np.std(historical_throughput, ddof=1)
    min_throughput = min(historical_throughput)
    max_throughput = max(historical_throughput)

    print("=" * 60)
    print(f"{sprint_name.upper()} COMPLETION FORECAST - MONTE CARLO SIMULATION")
    print("=" * 60)
    print(f"\nHistorical Throughput:")
    for i, throughput in enumerate(historical_throughput, 1):
        print(f"  Sprint {i}: {throughput} items")
    print(f"\n  Average: {avg_throughput:.2f} items")
    print(f"  Std Dev: {std_throughput:.2f} items")
    print(f"  Min: {min_throughput} items")
    print(f"  Max: {max_throughput} items")

    print(f"\n{sprint_name} Scope:")
    print(f"  Remaining to complete: {sprint_remaining} items")

    print(f"\nRunning {num_simulations:,} simulations...")

    # Run simulation
    successes = 0
    simulated_completions = []

    for _ in range(num_simulations):
        sprint_throughput = np.random.choice(historical_throughput)
        simulated_completions.append(sprint_throughput)

        if sprint_throughput >= sprint_remaining:
            successes += 1

    # Calculate results
    probability = (successes / num_simulations) * 100

    p50 = np.percentile(simulated_completions, 50)
    p75 = np.percentile(simulated_completions, 75)
    p85 = np.percentile(simulated_completions, 85)
    p95 = np.percentile(simulated_completions, 95)

    completion_counts = Counter(simulated_completions)

    # Print results
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"\n✨ PROBABILITY OF COMPLETING ALL {sprint_name.upper()} ITEMS: {probability:.1f}%")
    print(f"\n   ({successes:,} out of {num_simulations:,} simulations completed all {sprint_remaining} remaining items)")

    print(f"\nThroughput Percentiles:")
    print(f"  P50 (50th percentile): {p50:.0f} items")
    print(f"  P75 (75th percentile): {p75:.0f} items")
    print(f"  P85 (85th percentile): {p85:.0f} items")
    print(f"  P95 (95th percentile): {p95:.0f} items")

    print(f"\nThroughput Distribution (from {num_simulations:,} simulations):")
    for items in sorted(completion_counts.keys()):
        count = completion_counts[items]
        percentage = (count / num_simulations) * 100
        bar = "█" * int(percentage / 2)
        status = "✓ Completes" if items >= sprint_remaining else "✗ Incomplete"
        print(f"  {items:2d} items: {percentage:5.1f}% {bar} ({count:,}) {status}")

    # Determine confidence level
    if probability >= 85:
        confidence = "HIGH CONFIDENCE"
        emoji = "🟢"
        insight = "Very likely to complete"
    elif probability >= 70:
        confidence = "MODERATE-HIGH"
        emoji = "🟡"
        insight = "Good chance of completion"
    elif probability >= 50:
        confidence = "MODERATE"
        emoji = "🟠"
        insight = "About 50/50"
    else:
        confidence = "LOW"
        emoji = "🔴"
        insight = "Unlikely to complete all items"

    # Create visualization if output path provided
    if output_path:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
        fig.suptitle(f'{sprint_name} Completion Forecast - Monte Carlo Simulation',
                     fontsize=14, fontweight='bold')

        # Chart 1: Historical throughput
        ax1.bar(range(1, len(historical_throughput) + 1), historical_throughput,
                color=['#3498db'] * len(historical_throughput), alpha=0.7, edgecolor='black')
        ax1.axhline(y=sprint_remaining, color='#e74c3c', linestyle='--', linewidth=2,
                   label=f'{sprint_name} Target ({sprint_remaining} items)')
        ax1.axhline(y=avg_throughput, color='#2ecc71', linestyle='--', linewidth=2,
                   label=f'Average ({avg_throughput:.1f} items)')
        ax1.set_xlabel('Sprint', fontsize=11, fontweight='bold')
        ax1.set_ylabel('Items Completed', fontsize=11, fontweight='bold')
        ax1.set_title('Historical Throughput', fontsize=12, fontweight='bold')
        ax1.set_xticks(range(1, len(historical_throughput) + 1))
        ax1.set_xticklabels([f'Sprint {i}' for i in range(1, len(historical_throughput) + 1)])
        ax1.legend(loc='upper left')
        ax1.grid(axis='y', alpha=0.3)

        # Chart 2: Simulated distribution
        items_list = sorted(completion_counts.keys())
        counts_list = [completion_counts[items] for items in items_list]
        colors = ['#e74c3c' if items < sprint_remaining else '#2ecc71' for items in items_list]
        ax2.bar(items_list, counts_list, color=colors, alpha=0.7, edgecolor='black')
        ax2.axvline(x=sprint_remaining - 0.5, color='#e74c3c', linestyle='--', linewidth=2,
                   label=f'{sprint_name} Target ({sprint_remaining} items)')
        ax2.set_xlabel('Items Completed in Sprint', fontsize=11, fontweight='bold')
        ax2.set_ylabel(f'Frequency (out of {num_simulations:,} runs)', fontsize=11, fontweight='bold')
        ax2.set_title(f'Simulated Distribution\n{probability:.1f}% Probability of Completion',
                     fontsize=12, fontweight='bold')
        ax2.legend()
        ax2.grid(axis='y', alpha=0.3)

        # Add text annotation
        textstr = 'Green = Complete\nRed = Incomplete'
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        ax2.text(0.98, 0.97, textstr, transform=ax2.transAxes, fontsize=9,
                verticalalignment='top', horizontalalignment='right', bbox=props)

        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        print(f"\n📊 Chart saved to: {output_path}")

    # Print key insights
    print("\n" + "=" * 60)
    print("KEY INSIGHTS")
    print("=" * 60)
    print(f"\n• {sprint_name} has {sprint_remaining} remaining items to complete")
    print(f"• Historical average throughput: {avg_throughput:.1f} items per sprint")
    print(f"• {probability:.1f}% chance of completing all items")
    print(f"• Confidence level: {emoji} {confidence} - {insight}")
    print("\n" + "=" * 60)

    # Return results dict
    return {
        'probability': probability,
        'successes': successes,
        'total_runs': num_simulations,
        'confidence': confidence,
        'confidence_emoji': emoji,
        'insight': insight,
        'percentiles': {
            'p50': p50,
            'p75': p75,
            'p85': p85,
            'p95': p95
        },
        'distribution': dict(completion_counts),
        'historical_stats': {
            'average': avg_throughput,
            'std_dev': std_throughput,
            'min': min_throughput,
            'max': max_throughput,
            'data': historical_throughput
        },
        'sprint_remaining': sprint_remaining
    }


def main():
    parser = argparse.ArgumentParser(
        description='Monte Carlo simulation for sprint completion forecast'
    )
    parser.add_argument('historical', nargs='+', type=int,
                       help='Historical throughput (space-separated integers)')
    parser.add_argument('--remaining', '-r', type=int, required=True,
                       help='Remaining items to complete in target sprint')
    parser.add_argument('--sprint-name', '-s', type=str, default='Sprint',
                       help='Name of sprint being forecasted (default: "Sprint")')
    parser.add_argument('--simulations', '-n', type=int, default=10_000,
                       help='Number of simulation runs (default: 10,000)')
    parser.add_argument('--output', '-o', type=str,
                       help='Path to save chart image (optional)')

    args = parser.parse_args()

    try:
        results = run_forecast(
            historical_throughput=args.historical,
            sprint_remaining=args.remaining,
            sprint_name=args.sprint_name,
            num_simulations=args.simulations,
            output_path=args.output
        )
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
