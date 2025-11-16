import json
import re
import argparse
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="Validate numeric claims in LLM responses.")
    parser.add_argument("--stats", required=True, help="Path to data/stats.json")
    parser.add_argument("--results", default="results/manual_outputs.jsonl", help="Logged LLM responses")
    parser.add_argument("--out", default="results/validation_summary.csv", help="Output CSV file")
    args = parser.parse_args()

    # Load Syracuse WLAX stats
    stats = json.load(open(args.stats, "r", encoding="utf-8"))

    # Load LLM outputs
    rows = [json.loads(l) for l in open(args.results, "r", encoding="utf-8")]

    records = []

    # Check each LLM output
    for r in rows:
        text = r["response"]

        ok = 0        # number of correct numeric claims
        total = 0     # total numeric claims detected

        for p in stats["players"]:
            player_name = p["id"]

            for field in ["goals", "assists", "turnovers"]:
                # Regex to catch patterns like "Player A ... 75 goals"
                patt = re.compile(
                    rf"{re.escape(player_name)}.*?(\d+)\s+{field}",
                    re.IGNORECASE
                )
                m = patt.search(text)

                if m:
                    total += 1
                    claimed_value = int(m.group(1))
                    true_value = int(p[field])

                    if claimed_value == true_value:
                        ok += 1

        accuracy = ok / total if total else None

        records.append({
            "provider": r.get("provider", ""),
            "model": r.get("model", ""),
            "variant": r.get("variant", ""),
            "ok": ok,
            "total": total,
            "accuracy": accuracy
        })

    # Save results
    df = pd.DataFrame(records)
    df.to_csv(args.out, index=False)
    print(f"Validation summary saved → {args.out}")


if __name__ == "__main__":
    main()
