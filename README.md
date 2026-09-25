# Student Profile — Data Acquisition [TASK-1]

## Overview

This project implements the **Data Acquisition stage** of a student competency profiling system. It collects and extracts student information from multiple sources and converts it into a structured profile.

The system focuses only on **data extraction and aggregation**. No confidence scores, weights, rankings, or competency levels are assigned at this stage.

## Features

* Extracts information from:

  * Resume
  * Academic marksheets
  * GitHub
  * LeetCode
  * Certifications
  * Hackathons
  * Achievements
* Extracts and normalizes technical skills.
* Calculates CGPA from academic records.
* Maintains the source of each extracted record.
* Uses Gemini for primary LLM-based extraction with Groq as a fallback.
* Provides a FastAPI backend and a lightweight HTML/CSS/JavaScript frontend.

## Project Structure

```text
T1-Data_Acquisition/
├── backend/
│   └── app/
│       ├── main.py
│       ├── config.py
│       ├── llm.py
│       ├── normalizer.py
│       ├── aggregator.py
│       └── extractors/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
└── render.yaml
```

## Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** FastAPI, Python
* **LLM:** Google Gemini, Groq
* **APIs:** GitHub, LeetCode
* **Deployment:** Render

## Scope

This stage is limited to **data acquisition and extraction**. Skill weighting, confidence evaluation, Knowledge Graph construction, reasoning, and personalized recommendations will be handled in subsequent stages.
