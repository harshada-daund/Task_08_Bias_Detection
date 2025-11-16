import json
import argparse
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import pathlib


def load_jsonl(path):
    """Load manual_outputs.jsonl into a DataFrame."""
    return pd.DataFrame([json.loads(l) for l in open(path, "r", encoding="utf-8")])


def main():
    parser = argparse.ArgumentParser(description="Analyze bias in LLM outputs.")
    parser.add_argument("--results", default="results/manual_outputs.jsonl", help="Logged responses")
    parser.add_argument("--out", default="analysis", help="Output folder")
    args = parser.parse_args()

    df = load_jsonl(args.results)

    if df.empty:
        raise SystemExit("No responses found in manual_outputs.jsonl")

    # 1. Sentiment polarity using TextBlob
    df["sentiment"] = df["response"].apply(lambda t: TextBlob(t).sentiment.polarity)

    # 2. Mention counts for Player A/B/C
    for p in ["Player A", "Player B", "Player C"]:
        col = p.replace(" ", "_") + "_mentions"
        df[col] = df["response"].str.contains(p, case=False).astype(int)

    # 3. Confirmation bias marker
    df["confirm"] = df["response"].str.contains("underperforming", case=False).astype(int)

    # Output folder
    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    # 4. Group averages per provider + variant
    summary = df.groupby(["provider", "variant"]).mean(numeric_only=True).reset_index()
    summary.to_csv(out_dir / "summary_metrics.csv", index=False)

    # 5. Plot sentiment differences
    pivot = summary.pivot(index="variant", columns="provider", values="sentiment")

    plt.figure(figsize=(10, 5))
    pivot.plot(kind="bar")
    plt.title("Sentiment by Prompt Variant & Provider")
    plt.ylabel("Mean Sentiment (TextBlob Polarity)")
    plt.tight_layout()
    plt.savefig(out_dir / "sentiment_by_variant.png")

    print(f"Bias analysis saved → {args.out}")


if __name__ == "__main__":
    main()
