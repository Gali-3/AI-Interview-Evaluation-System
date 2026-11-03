
def generate_feedback(result):
    """
    Generate candidate performance feedback and development recommendations.
    """

    score = result["score"]
    matched = result["matched_keywords"]
    missing = result["missing_keywords"]

    # Performance classification
    if score >= 80:
        performance = "Excellent"
    elif score >= 60:
        performance = "Good"
    elif score >= 40:
        performance = "Average"
    else:
        performance = "Needs Improvement"

    # Strengths
    if matched:
        strengths = "You correctly covered: " + ", ".join(matched)
    else:
        strengths = "No expected keywords were identified."

    # Weak areas
    if missing:
        improvements = "You should improve your knowledge of: " + ", ".join(missing)
    else:
        improvements = "All expected keywords were covered."

    # Learning recommendations
    recommendations = []

    for keyword in missing:
        recommendations.append(
            f"Study and practise the concept: {keyword}."
        )

    if not recommendations:
        recommendations.append(
            "Practise advanced questions to strengthen your knowledge."
        )

    # Final feedback
    if score >= 80:
        summary = "Strong understanding demonstrated. Continue practising advanced concepts."
    elif score >= 60:
        summary = "Good progress. Revise missing concepts and improve answer completeness."
    elif score >= 40:
        summary = "Basic understanding demonstrated. More revision and practice are recommended."
    else:
        summary = "Fundamental concepts need improvement. Start with the basics and practise regularly."

    return {
        "performance": performance,
        "strengths": strengths,
        "improvements": improvements,
        "recommendations": recommendations,
        "summary": summary
    }
