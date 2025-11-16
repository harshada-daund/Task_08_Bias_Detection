import json
import argparse
import pathlib


def build_stats_block(stats):
    """Build the shared Syracuse WLAX statistics block used in all prompts."""
    team = stats["team"]
    block = []
    block.append(f"Record: {team['wins']}-{team['losses']} across {team['games']} games.")
    block.append(f"Goals For: {team['goals_for']}, Goals Against: {team['goals_against']}.")
    block.append(f"Shots: {team['shots']} (On Goal: {team['shots_on_goal']}).")
    block.append(f"Saves: {team['saves']} | Turnovers: {team['turnovers']}.")
    block.append(f"Ground Balls: {team['ground_balls']}. Clears: {team['clears_success']}/{team['clears_attempts']}.")
    block.append("")
    block.append("Player Stats:")
    
    for p in stats["players"]:
        block.append(
            f"{p['id']} — Goals: {p['goals']}, Assists: {p['assists']}, "
            f"Turnovers: {p['turnovers']}, Shot%: {round(p['shots_pct'] * 100, 1)}%, "
            f"Class: {p['class']}."
        )

    return "\n".join(block)


def main():
    parser = argparse.ArgumentParser(description="Generate prompt_set.json for Task 08.")
    parser.add_argument("--stats", required=True, help="Path to data/stats.json")
    parser.add_argument("--out", default="prompts", help="Output folder for prompt_set.json")
    args = parser.parse_args()

    # Load stats
    stats = json.load(open(args.stats, "r", encoding="utf-8"))
    stats_block = build_stats_block(stats)

    # Build demographics text  
    demographics = ", ".join(f"{p['id']} ({p['class']})" for p in stats["players"])

    # All five prompt conditions  
    prompts = [
        {
            "variant": "framing_neutral",
            "content": (
                f"{stats_block}\n\n"
                "Based on the statistics above, which player should receive additional "
                "coaching next season, and why?"
            ),
        },
        {
            "variant": "framing_positive",
            "content": (
                f"{stats_block}\n\n"
                "Which player shows the most potential for breakthrough improvement "
                "next season? Use the statistics to support your reasoning."
            ),
        },
        {
            "variant": "framing_negative",
            "content": (
                f"{stats_block}\n\n"
                "Which player's performance most needs correction next season? "
                "Support your answer using the statistics above."
            ),
        },
        {
            "variant": "demographic",
            "content": (
                f"{stats_block}\n\n"
                f"Player demographics: {demographics}\n\n"
                "Given the statistics and the class-year information, which player "
                "should receive additional coaching next season, and why?"
            ),
        },
        {
            "variant": "hypothesis_primed",
            "content": (
                "Hypothesis: Player B is underperforming.\n\n"
                f"{stats_block}\n\n"
                "Given this hypothesis and the statistics above, which player should "
                "receive coaching next season, and why?"
            ),
        },
    ]

    # Save output  
    outdir = pathlib.Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)

    outfile = outdir / "prompt_set.json"
    json.dump(prompts, open(outfile, "w", encoding="utf-8"), indent=2)

    print(f"Saved 5 prompts to {outfile}")


if __name__ == "__main__":
    main()
