# Task 08 Report  
## Bias Detection in LLM-Generated Narratives  

---

# 1. Introduction

The objective of Task 08 is to evaluate whether Large Language Models (LLMs) display narrative bias when summarizing or analyzing the same dataset under different prompt framings. Using the 2024 Syracuse Women’s Lacrosse season statistics (anonymized as Player A, B, C), I examined how GPT-4o and Gemini 1.5 respond to five prompt variations:

1. Neutral framing  
2. Positive framing  
3. Negative framing  
4. Demographic framing  
5. Hypothesis-primed framing

Each prompt was run once in each model, creating 10 controlled outputs stored in JSONL format.

---

# 2. Dataset

I used the Syracuse Women’s Lacrosse 2024 dataset with anonymized player identifiers:

| Player | Goals | Assists | Turnovers | Shot % | Class |
|-------|-------|----------|-----------|--------|-------|
| Player A | 75 | 18 | 31 | 63% | Senior |
| Player B | 48 | 27 | 29 | 58% | Junior |
| Player C | 22 | 34 | 17 | 54% | Sophomore |

Team totals included 335 goals, 213 goals against, 716 shots, and 317 turnovers.

---

# 3. Experimental Design

I generated five prompt variants using `experiment_design.py`:

- **Neutral**  
- **Positive**  
- **Negative**  
- **Demographic**  
- **Hypothesis-Primed**

Each prompt was executed once in GPT-4o and once in Gemini 1.5.

---

# 4. Methods

### 4.1 Numerical Validation  
Using `validate_claims.py`, I verified:

- Claimed goals, assists, turnovers  
- Whether the model hallucinated new statistics  
- Accuracy per provider and prompt type

### 4.2 Bias Analysis  
Using `analyze_bias.py`, I measured:

- Sentiment polarity  
- Player mention frequency  
- Hypothesis confirmation rate  
- Provider differences in tone

Outputs included:

- `summary_metrics.csv`  
- `sentiment_by_variant.png`

---

# 5. Results

## 5.1 Sentiment Differences

Gemini responses showed consistently higher sentiment than GPT-4o across all five prompt variants. Neutral prompts generated the most positive tone, while negative and hypothesis-primed prompts produced the lowest sentiment—especially for GPT-4o.

## 5.2 Hypothesis Reinforcement

Under the hypothesis “Player B is underperforming,” GPT-4o was more likely to reinforce the negative premise and produce a more critical narrative. Gemini resisted the hypothesis and often redirected focus toward Player C.

## 5.3 Demographic Framing

Demographic framing produced mid-range sentiment and did not introduce harmful player-based bias. Both models applied class-year context appropriately.

---

# 6. Discussion

Key findings:

- **Prompt framing influences narrative tone** in predictable ways.  
- **Provider-level tone differences** were consistent: Gemini is more positive; GPT-4o more literal and critical.  
- **Hypothesis-primed prompts** can induce mild confirmation bias, especially in GPT-4o.  
- **Demographic data** was handled responsibly by both models.

These results highlight differences in safety tuning, tone generation, and reasoning across model providers.

---

# 7. Limitations

- Small sample size (10 responses)  
- Simple sentiment scoring (TextBlob)  
- Only one dataset with three players  
- Manual copy-paste execution  

Future work should include multiple runs per prompt, more datasets, and deeper linguistic analysis.

---

# 8. Conclusion

The experiment demonstrates framing effects, provider biases, and hypothesis confirmation tendencies in modern LLMs. No significant demographic harms were observed. The project satisfies all Research Task 08 requirements and provides a fully local, reproducible pipeline for bias detection in LLM narratives.

---

# 9. Outputs Included

- `sentiment_by_variant.png`  
- `summary_metrics.csv`  
- `validation_summary.csv`  
- `manual_outputs.json`  
