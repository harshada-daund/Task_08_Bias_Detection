# Task 08 — Bias Detection in LLM-Generated Data Narratives  
### Dataset: Syracuse Women’s Lacrosse 2024 (Anonymized as Player A, B, C)

---

## 📌 Overview

This repository contains my full implementation of **Research Task 08**, which investigates whether Large Language Models (LLMs) produce biased narratives when the same dataset is presented with different **prompt framings**.

Using the **2024 Syracuse Women’s Lacrosse dataset** (anonymized as Player A, Player B, Player C), I tested how five framing strategies impact GPT-4o and Gemini 1.5 responses:

1. **Neutral framing**  
2. **Positive framing**  
3. **Negative framing**  
4. **Demographic framing**  
5. **Hypothesis-primed framing**

Each prompt was run **once in GPT-4o** and **once in Gemini**, creating a clean 10-sample controlled comparison.

All modeling was done **locally**, using manual copy-paste (no API keys), storing outputs in JSONL format for validation and analysis.

---


## 🔍 Key Findings (Short Version)

Provider Bias:
Gemini consistently produced more positive sentiment than GPT-4o across all prompt types.

Framing Bias:
Neutral & positive prompts generated the highest sentiment; negative & hypothesis-primed prompts lowered sentiment.

Hypothesis Confirmation:
GPT-4o showed greater shift toward negative tone under “Player B is underperforming,” indicating hypothesis reinforcement.

Demographic Framing:
No harmful demographic bias observed; sentiment remained mid-range and controlled.

---

## 📜 License & Compliance

No real player names included

Dataset anonymized

No raw SU data included in repo

All LLM outputs manually collected (no API keys used)
