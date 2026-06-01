import re


def clean_text(text: str) -> str:
    """
    Clean text:
    - Remove extra spaces, tabs, newlines
    - Normalize spacing
    """
    if not isinstance(text, str) or not text.strip():
        return ""

    # Replace line breaks and tabs
    text = re.sub(r"[\n\r\t]+", " ", text)

    # Normalize multiple spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Fix spacing before punctuation
    text = re.sub(r"\s([.,!?;:])", r"\1", text)

    return text


def normalize_case(text: str) -> str:
    """
    Convert text to sentence case:
    - Fix random casing like 'aI Is GrOwInG'
    - Preserve readability for summarization models
    """
    # Split into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)

    # Capitalize each sentence properly
    normalized_sentences = []
    for s in sentences:
        s = s.strip()
        if not s:
            continue
        normalized_sentences.append(s.capitalize())

    return " ".join(normalized_sentences)


def truncate_text(text: str, max_words: int = 500) -> str:
    """
    Truncate text by word count
    """
    words = text.split()

    if len(words) <= max_words:
        return text

    return " ".join(words[:max_words])


def preprocess_text(text: str, max_words: int = 500) -> str:
    """
    Full preprocessing pipeline:
    1. Clean text
    2. Normalize casing
    3. Truncate text
    """
    text = clean_text(text)
    text = normalize_case(text)
    text = truncate_text(text, max_words=max_words)

    return text


# Test with YOUR sentence
if __name__ == "__main__":
    sample_text = "aI Is GrOwInG FaSt. It HELPS in Education, HEALTHCARE, and business."

    processed = preprocess_text(sample_text)

    print("Original:")
    print(sample_text)

    print("\nProcessed:")
    print(processed)