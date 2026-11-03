
from keyword_matcher import match_keywords
from ai_evaluator import generate_feedback
from interview_questions import interview_questions
from report_generator import generate_pdf_report


print("\n====================================")
print("     AI INTERVIEW EVALUATION")
print("====================================")

candidate_name = input("\nEnter candidate name: ")

all_results = []
total_score = 0

# Loop through all interview questions
for index, item in enumerate(interview_questions, start=1):

    question = item["question"]
    expected_keywords = item["expected_keywords"]

    print(f"\nQuestion {index}: {question}")

    candidate_answer = input("Enter your answer: ")

    # Compare candidate answer with expected keywords
    result = match_keywords(
        expected_keywords,
        candidate_answer
    )

    # Generate development feedback
    feedback = generate_feedback(result)

    total_score += result["score"]

    # Display question evaluation
    print("\n--- Evaluation Result ---")

    print("Matched Keywords:", result["matched_keywords"])
    print("Missing Keywords:", result["missing_keywords"])
    print("Score:", result["score"], "%")
    print("Performance:", feedback["performance"])

    # Store results
    all_results.append({
        "question": question,
        "candidate_answer": candidate_answer,
        "result": result,
        "feedback": feedback
    })


# Calculate overall interview score
overall_score = round(
    total_score / len(interview_questions), 2
)

print("\n====================================")
print("       FINAL INTERVIEW REPORT")
print("====================================")

print("Candidate:", candidate_name)
print("Total Questions:", len(interview_questions))
print("Overall Score:", overall_score, "%")

# Generate combined PDF using the first question for now
# We will upgrade the PDF generator in the next step.
pdf_file = generate_pdf_report(
    candidate_name,
    all_results,
    overall_score
)

print("\nPDF report generated successfully!")
print("Report location:", pdf_file)
print("\nInterview evaluation completed!")
