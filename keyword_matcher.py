
import re

# Alternative expressions for expected keywords
KEYWORD_ALIASES = {
    "object-oriented": ["object oriented", "oop"],
    "platform independent": ["platform-independent"],
    "bytecode": ["byte code"]
}


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def match_keywords(expected_keywords, candidate_answer):

    cleaned_answer = clean_text(candidate_answer)

    matched_keywords = []
    missing_keywords = []

    for keyword in expected_keywords:

        cleaned_keyword = clean_text(keyword)

        alternatives = KEYWORD_ALIASES.get(
            cleaned_keyword, []
        )

        search_terms = [cleaned_keyword] + alternatives

        found = False

        for term in search_terms:

            cleaned_term = clean_text(term)

            pattern = r'\b' + re.escape(cleaned_term) + r'\b'

            if re.search(pattern, cleaned_answer):
                found = True
                break

        if found:
            matched_keywords.append(keyword)
        else:
            missing_keywords.append(keyword)

    total_keywords = len(expected_keywords)

    score = (
        len(matched_keywords) / total_keywords * 100
        if total_keywords > 0 else 0
    )

    return {
        "total_keywords": total_keywords,
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords,
        "score": round(score, 2)
    }
