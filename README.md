# AI Interview Evaluation System

An AI-assisted interview evaluation project that analyzes candidate answers using keyword matching, calculates performance scores, and generates detailed PDF evaluation reports.

## Project Overview

The system evaluates candidate responses to technical interview questions by comparing answers against predefined expected keywords.

It identifies strengths, missing concepts, performance levels, and areas for improvement.

## Features

- Multiple technical interview questions
- Candidate answer collection
- Automatic keyword matching
- Matched and missing keyword identification
- Individual question score calculation
- Overall interview score calculation
- Performance classification
- Personalized development feedback
- PDF interview report generation

## Technologies Used

- Python
- Regular Expressions
- ReportLab
- PDF Generation

## Project Structure

```text
key word mather/
│
├── main.py
├── keyword_matcher.py
├── ai_evaluator.py
├── interview_questions.py
├── report_generator.py
├── reports/
├── .gitignore
└── README.md
```

## How It Works

1. Candidate enters their name.
2. The system displays technical interview questions.
3. Candidate submits answers.
4. Answers are checked against expected keywords.
5. Matched and missing keywords are identified.
6. Scores and performance feedback are calculated.
7. A detailed PDF report is generated.

## How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd "key word mather"
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install reportlab
```

### 6. Run the application

```bash
python main.py
```

## Evaluation Output

The system generates a PDF report containing:

- Candidate information
- Interview questions and answers
- Individual question scores
- Matched and missing keywords
- Strengths and improvement areas
- Learning recommendations
- Overall performance summary

## Current Limitation

The current evaluation module uses rule-based keyword matching and predefined expected keywords. It does not yet perform semantic answer evaluation.

## Future Enhancements

- AI-based semantic answer evaluation
- Dynamic interview question generation
- Integration with an AI interview platform
- Candidate performance analytics
- Web-based interview dashboard

## Author

**Siva Narayana**

GitHub: https://github.com/Gali-3