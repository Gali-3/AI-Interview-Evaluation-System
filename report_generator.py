
import os
import re
from datetime import datetime
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)


def generate_pdf_report(candidate_name, all_results, overall_score):

    # Create reports folder
    os.makedirs("reports", exist_ok=True)

    # Clean candidate name for filename
    safe_name = re.sub(r'[^A-Za-z0-9_-]', '_', candidate_name)

    file_name = os.path.join(
        "reports",
        f"{safe_name}_interview_report.pdf"
    )

    # Create PDF document
    document = SimpleDocTemplate(
        file_name,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    heading_style = styles["Heading2"]
    normal_style = styles["BodyText"]

    small_style = ParagraphStyle(
        "Small",
        parent=normal_style,
        fontSize=9,
        leading=13
    )

    story = []

    # ==============================
    # REPORT TITLE
    # ==============================

    story.append(
        Paragraph(
            "AI INTERVIEW EVALUATION REPORT",
            title_style
        )
    )

    story.append(Spacer(1, 15))

    # ==============================
    # CANDIDATE DETAILS
    # ==============================

    story.append(
        Paragraph(
            f"<b>Candidate Name:</b> {escape(candidate_name)}",
            normal_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Date:</b> {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            normal_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Total Questions:</b> {len(all_results)}",
            normal_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Overall Score:</b> {overall_score}%",
            normal_style
        )
    )

    story.append(Spacer(1, 20))

    # ==============================
    # INDIVIDUAL QUESTION REPORTS
    # ==============================

    for index, item in enumerate(all_results, start=1):

        question = escape(str(item["question"]))
        candidate_answer = escape(str(item["candidate_answer"]))

        result = item["result"]
        feedback = item["feedback"]

        story.append(
            Paragraph(
                f"Question {index}: {question}",
                heading_style
            )
        )

        story.append(Spacer(1, 8))

        story.append(
            Paragraph(
                "<b>Candidate Answer:</b>",
                normal_style
            )
        )

        story.append(
            Paragraph(
                candidate_answer if candidate_answer else "No answer provided.",
                small_style
            )
        )

        story.append(Spacer(1, 8))

        story.append(
            Paragraph(
                f"<b>Matching Score:</b> {result['score']}%",
                normal_style
            )
        )

        story.append(
            Paragraph(
                f"<b>Performance:</b> {escape(str(feedback['performance']))}",
                normal_style
            )
        )

        story.append(Spacer(1, 8))

        # Keyword evaluation table
        matched = ", ".join(result["matched_keywords"]) or "None"
        missing = ", ".join(result["missing_keywords"]) or "None"

        table_data = [
            [
                Paragraph("<b>Matched Keywords</b>", small_style),
                Paragraph("<b>Missing Keywords</b>", small_style)
            ],
            [
                Paragraph(escape(matched), small_style),
                Paragraph(escape(missing), small_style)
            ]
        ]

        keyword_table = Table(
            table_data,
            colWidths=[250, 250]
        )

        keyword_table.setStyle(
            TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("PADDING", (0, 0), (-1, -1), 8)
            ])
        )

        story.append(keyword_table)

        story.append(Spacer(1, 10))

        # Strengths
        story.append(
            Paragraph(
                f"<b>Strengths:</b> {escape(str(feedback['strengths']))}",
                small_style
            )
        )

        story.append(Spacer(1, 5))

        # Areas to improve
        story.append(
            Paragraph(
                f"<b>Areas to Improve:</b> {escape(str(feedback['improvements']))}",
                small_style
            )
        )

        story.append(Spacer(1, 5))

        # Learning recommendations
        story.append(
            Paragraph(
                "<b>Learning Recommendations:</b>",
                normal_style
            )
        )

        for recommendation in feedback["recommendations"]:
            story.append(
                Paragraph(
                    "• " + escape(str(recommendation)),
                    small_style
                )
            )

        story.append(Spacer(1, 5))

        # Development summary
        story.append(
            Paragraph(
                f"<b>Development Summary:</b> {escape(str(feedback['summary']))}",
                small_style
            )
        )

        story.append(Spacer(1, 20))

    # ==============================
    # OVERALL DEVELOPMENT SUMMARY
    # ==============================

    story.append(
        Paragraph(
            "FINAL DEVELOPMENT SUMMARY",
            heading_style
        )
    )

    if overall_score >= 80:
        recommendation = (
            "Excellent performance. Continue practising advanced "
            "technical interview questions."
        )

    elif overall_score >= 60:
        recommendation = (
            "Good performance. Revise missing concepts and improve "
            "the completeness of your answers."
        )

    elif overall_score >= 40:
        recommendation = (
            "Average performance. Focus on strengthening technical "
            "knowledge and practising explanations."
        )

    else:
        recommendation = (
            "Needs improvement. Start with fundamental concepts "
            "and practise answering technical questions regularly."
        )

    story.append(
        Paragraph(
            f"<b>Overall Assessment:</b> {escape(recommendation)}",
            normal_style
        )
    )

    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            "Report generated by AI Interview Evaluation System.",
            small_style
        )
    )

    # ==============================
    # GENERATE PDF
    # ==============================

    document.build(story)

    return file_name
